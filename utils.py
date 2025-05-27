import re

def extract_link(text: str) -> str:
    match = re.search(r"(https://t\\.me/\\S+)", text)
    return match.group(1) if match else ""

def generate_mentions(users: list) -> str:
    return " ".join([f"[{u.first_name}](tg://user?id={u.id})" for u in users])
