import requests
import json

url = "http://localhost:5001/api/predict"

texts = [
    "Lord Rama is real or not?",
    "Lord Rama is real or not",  # No question mark
    "Lord Rama is real or not ", # Trailing space
    "Lord Rama is real or not."  # Period
]

for text in texts:
    payload = {
        "text": text,
        "model_type": "deep_learning",
        "region": "global"
    }
    response = requests.post(url, json=payload)
    print(f"Input: '{text}' -> Verdict: {response.json().get('final_verdict')}, Score: {response.json().get('ai_score')}")
