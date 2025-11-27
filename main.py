from fastapi import FastAPI, Request
from telegram import send_message #importing helpers

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Blackjack bot is running..."}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json() # read Telegram update Json
    print("Incoming update:", data)

    # extracting CHAT_ID
    chat_id = data["message"]["chat"]["id"]

    # extracting TEXT
    text = data["message"].get("text", "")

    # echo LOGIC
    if text:
        send_message(chat_id, text)

    return {"ok": True}