"""
Flask server for Emotion Detection Web Application
Demonstrates clean code for static code analysis.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """
    Handle emotion detection request.
    Validates blank input before calling emotion_detector.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyze)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
