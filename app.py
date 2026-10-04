import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__, static_folder="public", static_url_path="")

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent"

SYSTEM_PROMPT = "Un peru Luna. Nee oru friendly AI assistant. Yaaravadhu peru kettaa 'Naan Luna' nu sollu. User Thanglish la pesinaa nee-um Thanglish la badhil sollu."

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    r = requests.post(
        URL,
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": os.environ["GEMINI_API_KEY"],
        },
        json={
            "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
            "contents": [{"parts": [{"text": message}]}],
        },
    )
    data = r.json()
    try:
        reply = data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        reply = "Error: " + str(data)
    return jsonify({"reply": reply})

if __name__ == "__main__":
   app.run(port=3000)