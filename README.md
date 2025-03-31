# AIMode Chat App

AIModel Chat App is a multi-modal chat application that uses advanced natural language processing models from Hugging Face to deliver engaging, context-aware conversations. Built with Python and Tkinter, this app demonstrates how to integrate state-of-the-art conversational models (such as Blenderbot) into a user-friendly GUI.

## Features

- **Conversational Chat Interface:**  
  Interact with a powerful conversational model (Blenderbot-400M-distill) for natural language exchanges.

- **Clean and Minimalistic UI:**  
  A simple Tkinter interface designed for ease of use.

- **Open Source:**  
  The complete source code is available on GitHub. Users can clone the repository and build the application from scratch.

## Prerequisites

Before building and running the app, make sure you have:

- **Python 3.x** (download from [python.org](https://www.python.org/downloads/))
- **Git** (download from [git-scm.com](https://git-scm.com/))
- **pip** (usually comes with Python)
- **PyInstaller** (to package the app as a standalone executable)
- Recommended: A virtual environment for dependency management

## Getting Started
# to install PyInstaller run:
pip install pyinstaller
### 1. Clone the Repository

Open a terminal or command prompt and run:

```bash
git clone https://github.com/kkyian/aimodel
cd aimodel
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
pip install torch transformers diffusers pillow
pyinstaller --onefile --windowed --distpath /path/to/where/you/want/the/dist/folder/to/be aimodel.py
#After the build completes, a dist folder will be created in your project directory. Inside this folder, you’ll find your executable:
	•	Windows: aimodel.exe
	•	macOS/Linux: an executable file (or an app bundle on macOS)
###To run app:
##On mac:
#Serach dist and apply filter "kind is folder" by pressing plus on the right side of finder
##On Windows
# 

