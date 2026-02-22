"""
Flask server for Emotion Detection Web Application
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response is None or response == "Invalid text! Please try again.":
        return "Invalid text! Please try again."

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
