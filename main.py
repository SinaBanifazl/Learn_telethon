from telethon import TelegramClient, events
import time

API_ID = 28418618
API_HASH = "993aded4010f0bdf844dc777859516b8"
BOT_TOKEN = "7611699084:AAErPfRjOMYJVY7kfzlFkazXNyi8SwiKB4c"

client = TelegramClient("bot_session", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage)
async def message_handler(event):
    chat_id = event.chat_id
    text = event.text
    print(f"chat id shoma {chat_id} hast va text shoma {text} mibashad")

    if text == "/start":
        await client.send_message(chat_id, "به ربات ما خوش اومدی", reply_to=event.message.id)
        return
    elif text == "/close":
        await client.send_message(chat_id, "برنامه بسته شد", reply_to=event.message.id)
        return        
    
    me = await client.get_me()
    print(me.id)


print("bot is running...")
client.run_until_disconnected()