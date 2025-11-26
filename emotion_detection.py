import requests # Import the library "requests" to manage HTTP requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input, headers=headers) # Send a POST request to the API with text and headers
    return response.text