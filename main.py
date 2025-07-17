from telethon import TelegramClient, events
import time

API_ID = "28418618"
API_HASH = "993aded4010f0bdf844dc777859516b8"
BOT_TOKEN = "7611699084:AAErPfRjOMYJVY7kfzlFkazXNyi8SwiKB4c"

client = TelegramClient("bot_session", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# @client.on(events.NewMessage)
# async def message_handler(event):
#     chat_id = event.chat_id
#     text = event.text
#     print(f"chat id shoma {chat_id} hast va text shoma {text} mibashad")

#     if text == "/start":
#         await client.send_message(chat_id, "به ربات ما خوش اومدی", reply_to=event.message.id)
#         return
#     elif text == "/close":
#         await client.send_message(chat_id, "برنامه بسته شد", reply_to=event.message.id)
#         return        
    

    # await client.send_message(chat_id, 
    #                           f"<b>{text}</b> | بولد شده", 
    #                           reply_to=event.message.id, 
    #                           parse_mode="HTML"
    #                           )

    # files = [r"C:\Users\Sina Banifazl\Desktop\bot tel\Learn_telethon\1.png", r"C:\Users\Sina Banifazl\Desktop\bot tel\Learn_telethon\2.png"]
    # await client.send_file(chat_id, files, caption="این یک فایل تست است", force_document=True)

@client.on(events.NewMessage(pattern=r"/hi (.+)"))
async def handle(event):
    print(event.stringify())


print("bot is running...")
client.run_until_disconnected()