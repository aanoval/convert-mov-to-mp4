from flask import Flask, request, jsonify
import os
import subprocess
from pathlib import Path
import uuid

app = Flask(__name__)

def check_ffmpeg():
    """Check if FFmpeg is installed."""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def convert_mov_to_mp4(input_file, output_file, overwrite=False):
    """Convert MOV file to MP4 using FFmpeg."""
    try:
        # Validate input file
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file {input_file} not found")
        
        if not input_file.lower().endswith('.mov'):
            raise ValueError("Input file must have .mov extension")

        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        # FFmpeg command for conversion
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', input_file,
            '-vcodec', 'h264',
            '-acodec', 'aac',
            '-strict', '-2'
        ]
        
        if overwrite:
            ffmpeg_cmd.append('-y')
        
        ffmpeg_cmd.append(output_file)

        # Run conversion
        result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, check=True)
        return {"status": "success", "message": f"Conversion successful: {output_file}"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": f"Conversion error: {e.stderr}"}
    except Exception as e:
        return {"status": "error", "message": f"Error: {str(e)}"}

@app.route('/')
def serve_index():
    """Serve the HTML UI."""
    return app.send_static_file('index.html')

@app.route('/convert', methods=['POST'])
def convert_video():
    """Handle video conversion request."""
    if not check_ffmpeg():
        return jsonify({"status": "error", "message": "FFmpeg not found. Please install FFmpeg first (brew install ffmpeg)."})

    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file uploaded"})
    
    file = request.files['file']
    output_filename = request.form.get('output_filename', 'output.mp4')
    overwrite = request.form.get('overwrite', 'false').lower() == 'true'

    # Save temporary file
    temp_dir = os.path.join(os.getcwd(), 'temp')
    os.makedirs(temp_dir, exist_ok=True)
    input_path = os.path.join(temp_dir, str(uuid.uuid4()) + '.mov')
    file.save(input_path)

    # Determine output path
    output_dir = os.path.join(os.getcwd(), 'output')
    output_path = os.path.join(output_dir, output_filename)

    # Convert file
    result = convert_mov_to_mp4(input_path, output_path, overwrite)

    # Clean up temporary file
    if os.path.exists(input_path):
        os.remove(input_path)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)