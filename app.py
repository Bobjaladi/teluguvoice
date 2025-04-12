from flask import Flask, render_template, request, send_file
import os
from gtts import gTTS

app = Flask(__name__)

UPLOAD_FOLDER = "static"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get text input from user
        text = request.form["description"]
        
        # Convert text to Telugu speech
        tts = gTTS(text, lang="te")
        audio_path = os.path.join(UPLOAD_FOLDER, "audio.mp3")
        tts.save(audio_path)
        
        return render_template("index.html", audio_generated=True, audio_path=audio_path)

    return render_template("index.html", audio_generated=False)

@app.route("/download")
def download():
    return send_file("static/audio.mp3", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
