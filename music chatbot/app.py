import json
from datetime import datetime
from pathlib import Path

from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)
HISTORY_FILE = Path(app.root_path) / "chat_history.json"

genai.configure(api_key="AIzaSyBkwR3HT0uyIkbScK06hB25wUdyswpDD3Y")

# Use a supported model name for generate_content. "gemini-2.5-flash" is currently available.
model = genai.GenerativeModel("gemini-2.5-flash")


def load_chat_history():
    if not HISTORY_FILE.exists():
        return []

    try:
        with HISTORY_FILE.open("r", encoding="utf-8") as history_file:
            return json.load(history_file)
    except (json.JSONDecodeError, OSError):
        app.logger.exception("Error loading chat history")
        return []


def save_chat_history(history):
    with HISTORY_FILE.open("w", encoding="utf-8") as history_file:
        json.dump(history, history_file, indent=2)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/history", methods=["GET"])
def history():
    return jsonify({"history": load_chat_history()})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    try:
        response = model.generate_content(user_message)
        reply_text = response.text

        history = load_chat_history()
        history.append(
            {
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "user": user_message,
                "bot": reply_text,
            }
        )
        save_chat_history(history)

        return jsonify({"reply": reply_text})
    except Exception as e:
        # Log the error and return a JSON error response.
        app.logger.exception("Error generating response")
        return jsonify({"error": "Failed to generate response", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5001)
