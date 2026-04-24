import requests
from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()
API_key = os.getenv("API_key")

URL = "https://www.googleapis.com/youtube/v3/commentThreads"
params = {
    "videoId": "qUbxJ3PzMDk",
    "key": API_key,
    "part": "snippet,replies",
    "textFormat": "plainText"
}

response = requests.get(URL, params = params)
data = response.json()

def extract_comments(data):
    comments = []

    for item in data.get("items", []):
        try:
            text = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
            comments.append(text)
        except KeyError:
            continue

    return comments


comments = extract_comments(data)

print(comments)

#sentimentmodel = pipeline("sentiment-analysis")

#output = sentimentmodel("Bullshit ! How much they pay You ???")

#print(output)
