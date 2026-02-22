"""
Emotion Detection Application using Watson NLP
"""

import requests

def emotion_detector(text_to_analyze):
    """
    This function sends text to the Watson NLP emotion detection API
    and returns the detected emotions with their scores.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=headers)

    if response.status_code == 200:
        formatted_response = response.json()
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        return {
            "anger": emotions['anger'],
            "disgust": emotions['disgust'],
            "fear": emotions['fear'],
            "joy": emotions['joy'],
            "sadness": emotions['sadness']
        }
    else:
        return None


# Example test
if __name__ == "__main__":
    text = "I am very happy today!"
    result = emotion_detector(text)
    print(result)
