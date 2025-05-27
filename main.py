from pyrogram import Client, filters from pyrogram.types import Message from config import API_ID, API_HASH, BOT_TOKEN from utils import extract_link, generate_mentions import asyncio

app = Client("tagall_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command(["utag", "tagall"]) & filters.group) async def tag_all(client: Client, message: Message): user_ids = [] async for member in client.get_chat_members(message.chat.id): if not member.user.is_bot: user_ids.append(member.user)

text_args = message.text.split(maxsplit=1)
custom_text = text_args[1] if len(text_args) > 1 else "Panggilan semuanya!"

link = extract_link(custom_text)
if link:
    custom_text = custom_text.replace(link, "").strip()

batch_size = 5
for i in range(0, len(user_ids), batch_size):
    mention_text = generate_mentions(user_ids[i:i + batch_size])
    await message.reply(f"{custom_text}\n{mention_text}\n\n{link if link else ''}", disable_web_page_preview=True)
    await asyncio.sleep(2)

if name == "main": app.run()

