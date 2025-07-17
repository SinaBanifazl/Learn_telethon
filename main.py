from telethon import TelegramClient, events

API_ID = "28418618"
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
    

    # await client.send_message(chat_id, 
    #                           f"<b>{text}</b> | بولد شده", 
    #                           reply_to=event.message.id, 
    #                           parse_mode="HTML"
    #                           )
    # await client.send_message(chat_id, 
    #                           f"<i>{text}</i> | کج شده", 
    #                           reply_to=event.message.id, 
    #                           parse_mode="HTML"
    #                           )
    # await client.send_message(chat_id, 
    #                           f"<code>{text}</code> | کد شده(قابل کپی با کلیک روی اون) ", 
    #                           reply_to=event.message.id, 
    #                           parse_mode="HTML"
    #                           )

    await event.reply("این پاسخم به پیامی که دادیه. میتونه تو گروه باشه یا پیوی خودم یا هر جایی. این مهمه که event فعال شده و من هر جا که پیام بدی بهت این جوابو میدم. دیگه مثل client.send.message نیست که بخوام ازت chat.id بگیرم.")


print("bot is running...")
client.run_until_disconnected()