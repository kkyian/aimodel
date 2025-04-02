import tkinter as tk
from tkinter import ttk, scrolledtext
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import torch

# Set device (GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load Blenderbot model and tokenizer (free to use)
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name).to(device)

# Create main Tkinter window
root = tk.Tk()
root.title("Chat with Blenderbot (with History)")

# Create a PanedWindow for a split interface
paned = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned.pack(fill="both", expand=True)

# Left frame for conversation history (history bar)
frame_history = ttk.Frame(paned, width=200, relief="sunken")
paned.add(frame_history, weight=1)

# Right frame for the chat conversation and input
frame_chat = ttk.Frame(paned, padding="10")
paned.add(frame_chat, weight=3)

# History bar (a Listbox that displays each conversation turn)
history_listbox = tk.Listbox(frame_history)
history_listbox.pack(fill="both", expand=True)

# Chat conversation display (scrolled text widget)
chat_display = scrolledtext.ScrolledText(frame_chat, wrap=tk.WORD, width=60, height=20, state="disabled")
chat_display.pack(pady=5)

# Entry widget for new messages
chat_entry = ttk.Entry(frame_chat, width=50)
chat_entry.pack(pady=5)
chat_entry.insert(0, "Hello!")

# Status label
status_label = ttk.Label(frame_chat, text="Ready")
status_label.pack()

# Global variable to store the conversation history (as a string)
conversation_history = ""

def send_message():
    global conversation_history
    user_msg = chat_entry.get().strip()
    if not user_msg:
        return

    # Update conversation history with user input
    conversation_history += f"User: {user_msg}\nBot: "
    
    # Update the chat display with the user message
    chat_display.config(state="normal")
    chat_display.insert(tk.END, f"User: {user_msg}\n")
    chat_display.config(state="disabled")
    chat_display.yview(tk.END)
    chat_entry.delete(0, tk.END)
    
    status_label.config(text="Bot is typing...")
    root.update()
    
    # Use the conversation history as context for Blenderbot
    inputs = tokenizer(conversation_history, return_tensors="pt").to(device)
    reply_ids = model.generate(
        **inputs,
        max_length=256,
        do_sample=True,
        temperature=0.7,
        top_p=0.95
    )
    generated = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    
    # Extract the new bot response (remove the prompt part)
    if generated.startswith(conversation_history):
        new_response = generated[len(conversation_history):].strip()
    else:
        new_response = generated.strip()
    
    if not new_response:
        new_response = "I'm not sure."
    
    # Append the new response to the conversation history
    conversation_history += new_response + "\n"
    
    # Update the chat display with the bot response
    chat_display.config(state="normal")
    chat_display.insert(tk.END, f"Bot: {new_response}\n\n")
    chat_display.config(state="disabled")
    chat_display.yview(tk.END)
    
    status_label.config(text="Ready")
    
    # Update the history bar (clear and add each line from conversation_history)
    history_listbox.delete(0, tk.END)
    for line in conversation_history.splitlines():
        if line.strip():
            history_listbox.insert(tk.END, line)

# Send button
send_button = ttk.Button(frame_chat, text="Send", command=send_message)
send_button.pack(pady=5)

root.mainloop()