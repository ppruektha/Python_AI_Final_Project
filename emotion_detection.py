import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    
    formatted_response = json.loads(response.text)

    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    emotion_dict = {'Anger': anger_score, 'Disgust': disgust_score, 'Fear': fear_score, 'Joy': joy_score, 'Sadness': sadness_score}
    
    # Initialize variables to track the key with the maximum value
    max_key = None
    max_value = float('-inf')  # Initialize to negative infinity

    # Loop through the dictionary to find the maximum value
    for key, value in emotion_dict.items():
        if value > max_value:
            max_value = value
            max_key = key

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': max_key}