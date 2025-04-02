import tkinter as tk
from tkinter import ttk, scrolledtext
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import torch

# Set device (GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load Blenderbot model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name).to(device)

class AIMODELAppV2:
    def __init__(self, root):
        self.root = root
        self.root.title("AIMODEL Chat App V2")

        # Default generation parameters
        self.max_length = 256
        self.temperature = 0.7
        self.top_p = 0.95

        # Set up a PanedWindow to split the UI into two panels
        self.paned = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.paned.pack(fill="both", expand=True)

        # Left frame: Conversation History (Listbox)
        self.frame_history = ttk.Frame(self.paned, width=200, relief="sunken")
        self.paned.add(self.frame_history, weight=1)
        self.history_listbox = tk.Listbox(self.frame_history)
        self.history_listbox.pack(fill="both", expand=True)

        # Right frame: Chat Interface
        self.frame_chat = ttk.Frame(self.paned, padding="10")
        self.paned.add(self.frame_chat, weight=3)
        self.chat_display = scrolledtext.ScrolledText(self.frame_chat, wrap=tk.WORD, width=60, height=20, state="disabled")
        self.chat_display.grid(row=0, column=0, columnspan=3, pady=5)

        self.chat_entry = ttk.Entry(self.frame_chat, width=50)
        self.chat_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        self.chat_entry.insert(0, "Hello!")

        self.send_button = ttk.Button(self.frame_chat, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=5, pady=5)

        # Settings button to adjust generation parameters
        self.settings_button = ttk.Button(self.frame_chat, text="Settings", command=self.open_settings)
        self.settings_button.grid(row=1, column=2, padx=5, pady=5)

        self.status_label = ttk.Label(self.frame_chat, text="Ready")
        self.status_label.grid(row=2, column=0, columnspan=3, sticky=tk.W)

        # Store the conversation history as a list of strings
        self.conversation_history = []

    def update_history_bar(self):
        """Refresh the left-side history Listbox."""
        self.history_listbox.delete(0, tk.END)
        for line in self.conversation_history:
            self.history_listbox.insert(tk.END, line)

    def append_chat_display(self, speaker, message):
        """Append a message to the chat display area."""
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, f"{speaker}: {message}\n")
        self.chat_display.config(state="disabled")
        self.chat_display.yview(tk.END)

    def send_message(self):
        user_msg = self.chat_entry.get().strip()
        if not user_msg:
            return

        # Update chat display and conversation history with the user's message
        self.append_chat_display("User", user_msg)
        self.conversation_history.append(f"User: {user_msg}")
        self.chat_entry.delete(0, tk.END)
        self.status_label.config(text="Bot is typing...")
        self.root.update()

        # Build the prompt with the full conversation history
        prompt = "\n".join(self.conversation_history) + "\nBot:"
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        reply_ids = model.generate(
            **inputs,
            max_length=self.max_length,
            do_sample=True,
            temperature=self.temperature,
            top_p=self.top_p,
        )
        generated_text = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
        # Remove the prompt portion to get only the bot's new response
        if generated_text.startswith(prompt):
            bot_response = generated_text[len(prompt):].strip()
        else:
            bot_response = generated_text.strip()
        if not bot_response:
            bot_response = "I'm not sure."

        # Update displays with the bot's response
        self.append_chat_display("Bot", bot_response)
        self.conversation_history.append(f"Bot: {bot_response}")
        self.update_history_bar()
        self.status_label.config(text="Ready")

    def open_settings(self):
        """Open a settings window to adjust generation parameters."""
        settings_win = tk.Toplevel(self.root)
        settings_win.title("Settings")

        # Label and Entry for Max Length
        ttk.Label(settings_win, text="Max Length:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        max_length_var = tk.StringVar(value=str(self.max_length))
        max_length_entry = ttk.Entry(settings_win, textvariable=max_length_var)
        max_length_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label and Entry for Temperature
        ttk.Label(settings_win, text="Temperature:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        temperature_var = tk.StringVar(value=str(self.temperature))
        temperature_entry = ttk.Entry(settings_win, textvariable=temperature_var)
        temperature_entry.grid(row=1, column=1, padx=5, pady=5)

        # Label and Entry for Top p
        ttk.Label(settings_win, text="Top p:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        top_p_var = tk.StringVar(value=str(self.top_p))
        top_p_entry = ttk.Entry(settings_win, textvariable=top_p_var)
        top_p_entry.grid(row=2, column=1, padx=5, pady=5)

        def save_settings():
            try:
                self.max_length = int(max_length_var.get())
                self.temperature = float(temperature_var.get())
                self.top_p = float(top_p_var.get())
                self.status_label.config(text="Settings updated.")
            except ValueError:
                self.status_label.config(text="Invalid settings input.")
            settings_win.destroy()

        save_button = ttk.Button(settings_win, text="Save", command=save_settings)
        save_button.grid(row=3, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AIMODELAppV2(root)
    root.mainloop()
