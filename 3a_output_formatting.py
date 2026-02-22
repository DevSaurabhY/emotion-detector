"""
Emotion Detection Application with Formatted Output
"""

import requests

def emotion_detector(text_to_analyze):
    """
    This function sends text to the Watson NLP emotion detection API
    and returns a formatted output string.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=headers)

    if response.status_code == 200:
        formatted_response = response.json()
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']

        # Find dominant emotion
        emotion_scores = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return (
            f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, "
            f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}."
        )

    else:
        return "Invalid text! Please try again."


# Example test
if __name__ == "__main__":
    text = "I am very happy today!"
    print(emotion_detector(text))
