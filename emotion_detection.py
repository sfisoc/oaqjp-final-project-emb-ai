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

    return response.text

    # print(response)

    # if response.status_code != 200:
    #     return {'label': None, 'score': None}

    # formatted_response = response.json()
    # document_sentiment = formatted_response.get('documentSentiment')

    # if not document_sentiment:
    #     return {'label': None, 'score': None}

    # return {
    #     'label': document_sentiment.get('label'),
    #     'score': document_sentiment.get('score')
    # }
    