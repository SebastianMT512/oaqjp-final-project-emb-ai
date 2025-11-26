import requests # Import the library "requests" to manage HTTP requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input, headers=headers) # Send a POST request to the API with text and headers
    formatted_response = json.loads(response.text)# Transform the response format in a dictionary with json.loads
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']# Extract the emotions from the response
        # Extract the scores from each emotion
        anger_score = emotions.get('anger')
        disgust_score = emotions.get('disgust')
        fear_score = emotions.get('fear')
        joy_score = emotions.get('joy')
        sadness_score = emotions.get('sadness')
        # Create a temporal dictionary with the emotions and their scores
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        # Find the emotion with the highest score
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    elif response.status_code == 500:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }