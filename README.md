# AIMODEL Chat App V3

An interactive AI chatbot desktop app built with Python, Tkinter, and Facebook's BlenderBot.

## 🚀 Features
- Chat interface with scrolling history
- Adjustable response generation (temperature, top-p, max length)
- Save and load conversations
- Responsive UI (multi-threaded)
- Built using Hugging Face Transformers

## 🛠️ Tech Stack
- Python 3
- Tkinter (GUI)
- Hugging Face Transformers
- BlenderBot 400M
- PyTorch

## 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/kkyian/aimodel.git
cd aimodel

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install torch transformers
#📦 Packaging the App with PyInstaller

#You can turn your Python app into a standalone executable:
pip install pyinstaller
pyinstaller --onefile --windowed aimodelv3
#This will generate a standalone executable in the dist/ folder.
