#This code create a project folder structure 

# Import necessary modules
import os
from pathlib import Path
import logging

# Configure how log messages will appear
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s :')

# List of files and folders to create for the project
list_of_files = [
    "src/__init__.py",         # Makes src a Python package
    "src/helper.py",           # Helper functions
    "src/prompt.py",           # Stores chatbot prompts or instructions
    ".env",                    # For storing environment variables (like API keys)
    "setup.py",                # Optional setup for packaging/installing
    "app.py",                  # Main application logic
    "research/trials.ipynb",   # Notebook for experiments
    "test.py"                  # Script for testing code
]

# Loop through each file in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to a Path object
    filedir, filename = os.path.split(filepath)  # Split into folder and file name

    # Create the folder if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create an empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
