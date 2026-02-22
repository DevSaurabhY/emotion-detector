"""
Emotion Detection Application
Returns structured dictionary output with dominant emotion.
"""

import requests


def emotion_detector(text_to_analyze):
    """
    Sends text to Watson NLP API and returns emotion scores
    in dictionary format including dominant_emotion.
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

    # Handle bad request
    if response.status_code == 400:
        return {
            "error": "Invalid text! Please try again."
        }

    if response.status_code == 200:
        formatted_response = response.json()
        emotions = formatted_response[
            "emotionPredictions"
        ][0]["emotion"]

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
        "error": "Error occurred while processing the request."
    }
