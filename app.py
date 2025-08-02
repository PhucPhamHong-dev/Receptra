import os
import json
import uuid
import hmac
import hashlib
import logging
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from markdown import markdown
from flask import Flask, render_template, redirect, url_for
# Load environment variables from .env
load_dotenv()
SECRET_KEY = os.getenv("FPT_WEBHOOK_SECRET")
BROKER_ID = os.getenv("FPT_BROKER_ID")
WEBHOOK_URL = os.getenv("FPT_WEBHOOK_URL")
VERIFY_TOKEN = os.getenv("FPT_VERIFY_TOKEN")

# Flask setup
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# Temporary storage for bot replies
last_bot_reply = {}
@app.route("/")
def root():
    return redirect(url_for("homepage"))
@app.route("/homepage", methods=["GET"])
def homepage():
    return render_template("homepage.html")

@app.route("/chat", methods=["GET"])
def chat_page():
    return render_template("chatbot.html")

@app.route("/chat-api", methods=["POST"])
def chat_api():
    """Handles incoming user messages and forwards them to the FPT webhook."""
    user_msg = request.json.get("message", "").strip()
    logging.debug(f"[RECEIVE] User message: {user_msg}")

    try:
        payload_dict = {
            "sender_id": "test_user_123",
            "sender_name": "Phúc",
            "broker_id": BROKER_ID,
            "message": {
                "mid": str(uuid.uuid4()),
                "text": user_msg
            }
        }
        payload_json = json.dumps(payload_dict, ensure_ascii=False)

        signature = hmac.new(
            SECRET_KEY.encode("utf-8"),
            payload_json.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        headers = {
            "Content-Type": "application/json",
            "X-Hub-Signature-256": f"sha256={signature}"
        }

        logging.debug(f"[CALL_API] POST {WEBHOOK_URL} payload={payload_json}")
        resp = requests.post(WEBHOOK_URL, data=payload_json.encode("utf-8"), headers=headers, timeout=10)
        resp.raise_for_status()
        logging.debug(f"[API_RESP] {resp.text}")
    except Exception:
        logging.exception("[ERROR] Failed to call FPT AI webhook")
        return jsonify({"error": "Unable to connect to FPT AI"}), 500
    global last_bot_reply
    last_bot_reply = {"reply": ""}
    return jsonify({"reply": "Message sent, awaiting reply at webhook"}), 200

@app.route("/indirect-channels/webhook/api", methods=["GET"])
def verify_webhook():
    """Handles webhook verification handshake via GET request."""
    challenge = request.args.get("challenge_code")
    token = request.args.get("verify_token")
    app.logger.debug(f"[VERIFY] challenge={challenge}, token_received={token}")
    if token != VERIFY_TOKEN:
        app.logger.warning(f"[VERIFY] Invalid token: {token}")
        return "Invalid token", 403
    return challenge, 200

@app.route("/indirect-channels/webhook/api", methods=["POST"])
def receive_webhook():
    """Receives and processes callback POST requests from the webhook."""
    # (Optional) HMAC verification
    signature = request.headers.get("X-Hub-Signature-256", "")
    if signature.startswith("sha256="):
        sig = signature.split("=", 1)[1]
        expected = hmac.new(
            SECRET_KEY.encode(), request.get_data(), hashlib.sha256
        ).hexdigest()
        if not hmac.compare_digest(sig, expected):
            app.logger.warning("[WEBHOOK] Invalid signature")
            return "Invalid signature", 403

    # Parse payload and update last_bot_reply
    data = request.get_json(force=True)
    payload = data.get("payload", {})
    if "text" in payload:
        raw_md = payload["text"].get("content", "")
        content_html = markdown(raw_md, extensions=['extra', 'sane_lists'])
        app.logger.info(f"[BOT REPLY - HTML] {content_html}")
        global last_bot_reply
        last_bot_reply = {"reply": content_html}

    return "OK", 200
@app.route("/services")
def services():
    return render_template("services.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/ourteam")
def ourteam():
    return render_template("ourteam.html")
@app.route("/latest-reply")
def get_latest():
    """Returns the latest reply received from the bot."""
    global last_bot_reply
    return jsonify(last_bot_reply)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)