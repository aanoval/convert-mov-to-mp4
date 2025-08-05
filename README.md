MOV to MP4 Converter
A simple web-based application to convert MOV video files to MP4 format using FFmpeg, optimized for MacBook Air M1. This project features a user-friendly interface built with HTML, JavaScript, and Tailwind CSS, and a Flask backend for handling conversions.
Features

Drag-and-Drop Interface: Upload MOV files by dragging or browsing.
Custom Output Filename: Specify the output MP4 filename.
Overwrite Option: Choose to overwrite existing files.
Progress Feedback: Visual progress bar and status messages.
Error Handling: Robust checks for FFmpeg installation, file validation, and conversion errors.
Optimized for M1: Uses FFmpeg optimized for Apple Silicon.

Prerequisites

macOS: Tested on MacBook Air M1.
Homebrew: Package manager for installing dependencies.
Python 3: Default on macOS.
FFmpeg: For video conversion.
Flask: Python web framework.

Installation

Install Homebrew (if not already installed):/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


Install FFmpeg:brew install ffmpeg


Install Python dependencies:pip install flask



Project Setup

Create a project directory:mkdir mov_to_mp4_converter
cd mov_to_mp4_converter


Save the following files in the project directory:
mov_to_mp4.py (backend)
static/index.html (frontend, create a static folder first)


Directory structure:mov_to_mp4_converter/
├── mov_to_mp4.py
├── static/
│   └── index.html
├── temp/ (auto-created)
├── output/ (auto-created)



Running the Application

Start the Flask server:python3 mov_to_mp4.py


Open a browser and navigate to http://localhost:5000.
Use the interface to:
Drag and drop a MOV file or click to browse.
Enter a custom output filename (optional, defaults to output.mp4).
Check "Overwrite if file exists" if needed.
Click "Convert" to start the process.


The converted MP4 file will be saved in the output folder.

Usage Notes

Output Location: Converted files are saved in the output directory in the project folder.
Temporary Files: Uploaded files are temporarily stored in the temp directory and automatically deleted after conversion.
File Support: Only .mov files are supported.
Accessibility: The UI includes ARIA attributes and clear feedback for better accessibility.

Troubleshooting

FFmpeg Not Found: Verify installation with ffmpeg -version. Reinstall if needed: brew install ffmpeg.
Port Conflict: If port 5000 is in use, change the port in mov_to_mp4.py (e.g., app.run(port=5001)).
Permission Issues: Ensure the project directory has write permissions for temp and output folders.
Large Files: Ensure sufficient disk space for temporary and output files.

Development Notes

Backend: Flask handles file uploads and FFmpeg conversion.
Frontend: Tailwind CSS for responsive styling, JavaScript for dynamic interactions.
Progress Bar: Simulated progress for user feedback (actual progress tracking requires FFmpeg integration, not implemented here).
M1 Optimization: FFmpeg via Homebrew is optimized for Apple Silicon.

Future Improvements

Add batch conversion support.
Implement real-time conversion progress using FFmpeg's progress output.
Add download link for converted files directly from the UI.
Support additional video formats.

License
This project is for personal use and provided as-is. Ensure you have the necessary licenses for FFmpeg and its dependencies.
For issues or feature requests, please contact the developer or submit a pull request.