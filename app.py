import os
import json
import uuid
import hmac
import hashlib
import logging
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

# Load .env
load_dotenv()
SECRET_KEY   = os.getenv("FPT_SECRET_KEY")
BROKER_ID    = os.getenv("FPT_BROKER_ID")
WEBHOOK_URL  = os.getenv("FPT_WEBHOOK_URL")
VERIFY_TOKEN = os.getenv("FPT_VERIFY_TOKEN")

# Flask setup
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# Bộ nhớ tạm lưu phản hồi bot
last_bot_reply = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "POST not allowed here", 405
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").strip()
    logging.debug(f"[RECEIVE] Người dùng: {user_msg}")

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
        logging.exception("[ERROR] Gọi FPT AI thất bại")
        return jsonify({"error": "Không thể kết nối đến FPT AI"}), 500

    return jsonify({"reply": "✅ Đã gửi message, chờ phản hồi tại webhook"}), 200

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    global last_bot_reply

    if request.method == "GET":
        challenge = request.args.get("challenge_code")
        token = request.args.get("verify_token")
        if token == VERIFY_TOKEN:
            logging.info("[WEBHOOK] Xác minh thành công")
            return challenge, 200
        else:
            logging.warning("[WEBHOOK] Xác minh thất bại")
            return "Token không hợp lệ", 403

    elif request.method == "POST":
        signature = request.headers.get("X-Hub-Signature-256", "").replace("sha256=", "")
        raw_body = request.get_data()
        computed_signature = hmac.new(
            SECRET_KEY.encode("utf-8"),
            raw_body,
            hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(signature, computed_signature):
            logging.warning("[WEBHOOK] Sai chữ ký")
            return "Invalid signature", 403

        try:
            data = request.json
            logging.info("[WEBHOOK] Nhận từ bot:\n" + json.dumps(data, indent=2, ensure_ascii=False))

            payload = data.get("payload", {})
            if "text" in payload:
                content = payload["text"]["content"]
                logging.info(f"[BOT REPLY] {content}")
                last_bot_reply = {"reply": content}
        except Exception:
            logging.exception("[WEBHOOK] Lỗi xử lý nội dung JSON")

        return "OK", 200

@app.route("/latest-reply")
def get_latest():
    global last_bot_reply
    return jsonify(last_bot_reply)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
