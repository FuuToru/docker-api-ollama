import requests
from fastapi import FastAPI, Response
import json

app = FastAPI()

SENTIMENT_MAPPING = {
    "neutral": 0,  # NEU
    "positive": 1,  # POS
    "negative": 2   # NEG
}

@app.get('/')
def home():
    return {"status": "Ok"}

@app.get('/ask')
def ask(prompt: str):
    res = requests.post('http://ollama:11434/api/generate', json={
        "prompt": f"""Hãy phân tích cảm xúc của câu sau về tập đoàn ggroup và chỉ trả về một trong ba nhãn sau mà không in thêm bất kỳ nội dung nào khác:
            - NEU (Trung lập)
            - POS (Tích cực)
            - NEG (Tiêu cực)
            Câu: "{prompt}"
            Chỉ trả lời bằng một từ duy nhất: NEU, POS, hoặc NEG.
            """,  
        "stream": False,
        "model": "llama3.2:1b"
    })
    return res.json().get("response", "").strip().lower()

    # if res.status_code != 200:
    #     return Response(content=json.dumps({"error": "Failed to get response from model"}), media_type="application/json", status_code=500)

    # response_text = res.json().get("response", "").strip().lower()

    # sentiment_value = SENTIMENT_MAPPING.get(response_text, 0)  

    # return {"sentiment": sentiment_value}
