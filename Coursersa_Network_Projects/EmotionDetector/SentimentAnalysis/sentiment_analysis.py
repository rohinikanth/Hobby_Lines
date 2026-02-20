import requests
import json


def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = response.json()

    if response.status_code == 200 and "documentSentiment" in formatted_response:
        label = formatted_response["documentSentiment"]["label"]
        score = formatted_response["documentSentiment"]["score"]
        return {"label": label, "score": score}
    elif response.status_code == 500:
        label = None
        score = None
    else:
        return {"error": formatted_response}