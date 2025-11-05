import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Request payload containing the text to analyze
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Header specifying the correct model ID for emotion analysis
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send POST request to the Watson NLP Emotion API
    response = requests.post(url, json=myobj, headers=headers)

    # Convert the response text (JSON string) to a Python dictionary
    formatted_response = json.loads(response.text)

    # Extract the emotion scores from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Extract individual emotion scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Find the dominant emotion (the one with the highest score)
    dominant_emotion = max(emotions, key=emotions.get)

    # Return the formatted dictionary
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }