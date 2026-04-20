import json
import os
from datetime import datetime

CHAT_DIR = "chats"
os.makedirs(CHAT_DIR, exist_ok=True)

def save_chat(chat_id, chat_name, messages):
    data = {
        "chat_id": chat_id,
        "chat_name": chat_name,
        "messages": messages,
        "updated_at": datetime.now().isoformat()
    }
    with open(os.path.join(CHAT_DIR, f"{chat_id}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_chat_safe(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def list_chats():
    chats = []
    for file in os.listdir(CHAT_DIR):
        if file.endswith(".json"):
            chat = load_chat_safe(os.path.join(CHAT_DIR, file))
            if chat:
                chats.append(chat)
    return sorted(chats, key=lambda x: x["updated_at"], reverse=True)

def generate_chat_name(prompt):
    prompt = prompt.strip()
    return prompt[:30] + "..." if len(prompt) > 30 else prompt
