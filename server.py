"""
Flask application for emotion detection using the EmotionDetection package.
Provides a web interface and API endpoint for analyzing emotions in text.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def detect_emotion():
    """Detect emotions in the provided text."""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response is None or response.get('dominant_emotion') is None:
        return 'Invalid text! Please try again.'

    return (
        'For the given statement, the system response is '
        f"'anger': {response.get('anger')}, "
        f"'disgust': {response.get('disgust')}, "
        f"'fear': {response.get('fear')}, "
        f"'joy': {response.get('joy')} and "
        f"'sadness': {response.get('sadness')}. "
        f"The dominant emotion is {response.get('dominant_emotion')}"
    )


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
