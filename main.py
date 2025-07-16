from telethon import TelegramClient, events

API_ID = "28418618"
API_HASH = "993aded4010f0bdf844dc777859516b8"
BOT_TOKEN = "7611699084:AAErPfRjOMYJVY7kfzlFkazXNyi8SwiKB4c"

client = TelegramClient("bot_session", API_ID, API_HASH).start(bot_token=BOT_TOKEN)



print("bot is running!")
print("==================")
client.run_until_disconnected()