# AIMode Chat App

AIMode Chat App is a multi-modal chat application that demonstrates how to integrate advanced natural language processing models from Hugging Face into a user-friendly GUI. Built using Python and Tkinter, this app provides engaging, context-aware conversations powered by models like Blenderbot.

## Features

- **Advanced Conversational AI:**  
  Uses Hugging Face's Blenderbot model for natural, context-aware responses.
- **Cross-Platform:**  
  Developed in Python with Tkinter for a simple yet effective GUI.
- **Open Source:**  
  The source code is available on GitHub so you can build and modify the app for personal use.

## Prerequisites

- **Python 3.x** (Download from [python.org](https://www.python.org/downloads/))
- **Git** (Download from [git-scm.com](https://git-scm.com/))
- **pip** (Usually comes with Python)
- **PyInstaller** (Used to package the app into a standalone executable)

## Getting Started

Follow these steps to clone the repository, install the dependencies, and build the executable.

### 1. Clone the Repository

Open a terminal or command prompt and run:

```bash
## git clone
git clone https://github.com/kkyian/aimodel.git
cd aimodel
## Create a virtual environment
### On mac do:
python3 -m venv venv
source venv/bin/activate
### On Windows:
python -m venv venv
venv\Scripts\activate
## Install dependencies
pip install torch transformers diffusers pillow pyinstaller
## Create app
### Make sure you cd the directory to aimodel.py
pyinstaller --onefile --windowed aimodel.py
### A folder will be in next to the aimodel.py which is called dist and inside you will find the app
