from flask import Flask, render_template, send_from_directory
from flask_compress import Compress



app = Flask(__name__)
# Enable GZIP compression
Compress(app)
# Path to your videos folder
VIDEO_FOLDER = "static/videos"

@app.route('/')
def index():
    # List video files in the video folder
    import os
    videos = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(('mp4', 'mkv', 'avi','jpg'))]
    return render_template('index.html', videos=videos)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/video/<filename>')
def video(filename):
    # Serve the video file
    return send_from_directory(VIDEO_FOLDER, filename)

if __name__ == "__main__":
    # Replace 0.0.0.0 with your local IP for external access
    app.run(host="0.0.0.0", port=5000, debug=True)
