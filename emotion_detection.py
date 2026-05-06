"""
Provides sentiment analysis functionality using the
IBM Watson Sentiment Analysis API.
"""

import requests

API_URL = (
    'https://sn-watson-emotion.labs.skills.network/v1/'
    'watson.runtime.nlp.v1/NlpService/EmotionPredict'
)

HEADERS = {
    'grpc-metadata-mm-model-id':
    'emotion_aggregated-workflow_lang_en_stock'
}


def emotion_detector(text_to_analyze):
    """
    Analyze the sentiment of the given text.

    :param text_to_analyze: Text input for sentiment analysis
    :type text_to_analyze: str
    :return: Dictionary containing sentiment label and score
    :rtype: dict
    """
    payload = {
        'raw_document': {
            'text': text_to_analyze
        }
    }

    response = requests.post(
        API_URL,
        json=payload,
        headers=HEADERS,
        timeout=10
    )

    if response.status_code != 200:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }

    formated_response = response.json()

    emotions = formated_response['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Return required format
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': max(emotions, key=emotions.get)
    }
    