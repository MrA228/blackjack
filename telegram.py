import requests
import os

TOKEN = os.getenv("BOT_TOKEN")

API_URL = f"https://api.telegram.org/bot{TOKEN}"

def send_message(chat_id: int, text: str):
    """Send a message to a Telegram CHAT"""
    url = f"{API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)