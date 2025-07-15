import os, requests
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("FPT_SECRET_KEY")      # bot token copy từ console
BOT_CODE  = os.getenv("FPT_BOT_CODE")        # ví dụ "01JZA4PCXJ1WZBAQ1PJZ0BFAJ6"
API_URL   = "https://bot.fpt.ai/api/get_answer/"

def get_bot_reply(user_text):
    payload = {
        "channel": "api",
        "app_code": BOT_CODE,
        "sender_id": "user_123",
        "type": "text",
        "message": {"type": "text", "content": user_text}
    }
    headers = {
        "Authorization": f"Bearer {BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    resp = requests.post(API_URL, json=payload, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return data.get("data", {}).get("answer", "🤔 Bot không trả lời được")

# Thử nghiệm
print(get_bot_reply("Xin chào"))
