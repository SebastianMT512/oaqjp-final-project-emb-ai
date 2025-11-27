"""
Flask application for emotion detection using Watson NLP API.
This module serves the web interface and processes text to detect emotions.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector


app = Flask(__name__)


def format_output(response):
    """
    Formats the emotion detection response into a human-readable string.

    Args:
        response (dict): Dictionary containing emotion scores and dominant emotion.

    Returns:
        str: Formatted string with emotion scores and dominant emotion.
    """
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Try again."

    output = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return output


@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint for emotion detection. Accepts text via query parameter 'textToAnalyze',
    processes it, and returns the formatted emotion analysis result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return format_output(response)


@app.route("/")
def render_index_page():
    """
    Renders the index.html page for the web interface.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    