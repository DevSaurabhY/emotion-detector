"""
Emotion Detection Application with Proper Error Handling
"""

import requests


def emotion_detector(text_to_analyze):
    """
    Sends text to Watson NLP emotion detection API
    and returns structured dictionary output.
    Handles 400 status code correctly.
    """

    url = "https://sn-watson-emotion.labs.skills.network/" \
          "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    # ✅ REQUIRED 400 HANDLING
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if response.status_code == 200:
        formatted_response = response.json()
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]

        emotion_scores = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }

        dominant_emotion = max(
            emotion_scores,
            key=emotion_scores.get
        )

        emotion_scores["dominant_emotion"] = dominant_emotion

        return emotion_scores

    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }
