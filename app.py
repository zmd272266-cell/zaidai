from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("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")
)

@app.route("/")
def home():
    return "ZaidAI Backend is Running!"

@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = client.responses.create(
            model="gpt-5",
            input=message
        )

        return jsonify({
            "reply": response.output_text
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
