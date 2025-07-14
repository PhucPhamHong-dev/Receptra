import os
import json
import uuid
import hmac
import hashlib
import requests
from dotenv import load_dotenv

# Load biến từ file .env
load_dotenv()

SECRET_KEY = os.getenv("FPT_SECRET_KEY")
BROKER_ID = os.getenv("FPT_BROKER_ID")
WEBHOOK_URL = "https://agents.fpt.ai/indirect-channels/webhook/api"  # luôn là URL này

def generate_signature(secret_key: str, body: str) -> str:
    hmac_digest = hmac.new(
        key=secret_key.encode("utf-8"),
        msg=body.encode("utf-8"),
        digestmod=hashlib.sha256
    ).hexdigest()
    return f"sha256={hmac_digest}"

def send_test_message(text: str):
    message_payload = {
        "sender_id": "test_user_123",
        "sender_name": "Phúc",
        "broker_id": BROKER_ID,
        "message": {
            "mid": str(uuid.uuid4()),
            "text": text
        }
    }

    body_json = json.dumps(message_payload, ensure_ascii=False)
    signature = generate_signature(SECRET_KEY, body_json)

    headers = {
        "Content-Type": "application/json",
        "X-Hub-Signature-256": signature
    }

    response = requests.post(WEBHOOK_URL, headers=headers, data=body_json)

    print(f"[STATUS] {response.status_code}")
    print(f"[RESPONSE] {response.text}")

if __name__ == "__main__":
    send_test_message("xin chào")  # Thay đổi nội dung message ở đây nếu muốn
