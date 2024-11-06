from flask import Flask, request, jsonify, render_template
from anthropic import Anthropic
import os, sys

app = Flask(__name__, template_folder="../frontend")

XAI_API_KEY = os.getenv("XAI_API_KEY")
client = Anthropic(api_key=XAI_API_KEY, base_url="https://api.x.ai")

@app.route('/grok')
def connect():
    return render_template("index.html")

@app.route('/send_message', methods=['POST']) #send_message
def send_message():
    data = request.get_json()
    user_message = data.get('message')

    response = client.messages.create(
        model="grok-beta",
        max_tokens=4096,
        system="You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy.",
        messages=[
            {"role": "user", "content": user_message},
        ]
    )
    print(response, file=sys.stderr)
    print("nano", file=sys.stderr)
    return jsonify({"response": response.content[0].text})

if __name__ == '__main__':
    app.run(host='0.0.0.0')

