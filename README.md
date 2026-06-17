# file-organizer
# File Organizer – Python Automation Tool

## Description
File Organizer is a Python-based automation tool designed to automatically organize files inside a directory into structured categories such as Images, Documents, Videos, and Others based on file extensions.

The purpose of this project is to reduce manual file management effort and demonstrate practical Python skills in automation and file system handling.

## Features
- Automatically detects file types based on extensions
- Organizes files into categories:
  - Images
  - Documents
  - Videos
  - Others
- Automatically creates required folders if they do not exist
- Moves files into the correct directories
- Simple command-line usage

## Technologies Used
- Python 3
- os module (file system operations)
- shutil module (file moving and management)

## How to Run

Clone the repository:
git clone https://github.com/your-username/file-organizer.git

Navigate into the project folder:
cd file-organizer

Run the program:
python main.py --source_dir /path/to/your/folder

Example:
python main.py --source_dir /Users/yourname/Desktop/test_files

## Project Structure
file-organizer/
│
├── main.py
├── test_files/
└── README.md

## Purpose
This project was built to practice Python automation, file handling, and working with the operating system. It demonstrates how Python can be used to create practical tools that improve productivity.

## Future Improvements
- Add graphical user interface (GUI) using Tkinter
- Add recursive folder scanning (subdirectories)
- Add duplicate file detection
- Add logging system for moved files
