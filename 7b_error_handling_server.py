"""
Flask server with blank input error handling
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

    # Handle blank input
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyze)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
