"""
Flask web application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotional Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the text provided in the query parameter `textToAnalyze` 
    and return the emotion analysis.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "No text provided! Please try again with a valid text."

    response = emotion_detector(text_to_analyze)
    anger = response.get('anger', 0)
    disgust = response.get('disgust', 0)
    fear = response.get('fear', 0)
    joy = response.get('joy', 0)
    sadness = response.get('sadness', 0)
    dominant_emotion = response.get('dominant_emotion', None)

    if dominant_emotion is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
