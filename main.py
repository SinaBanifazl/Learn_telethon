from telethon import TelegramClient, events
from telethon.tl.custom import Button

API_ID = 28418618
API_HASH = "993aded4010f0bdf844dc777859516b8"
BOT_TOKEN = "7611699084:AAErPfRjOMYJVY7kfzlFkazXNyi8SwiKB4c"

client = TelegramClient("bot_session", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage)
async def message_handler(event):
    text = event.text

    if text == "/start":
        keboard = [
            [Button.text("دکمه اول")]
        ]
        await event.reply("اینم از دکمه هاتون جناب", buttons=keboard)

print("bot is running...")
client.run_until_disconnected()