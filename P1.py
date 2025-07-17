from telethon import TelegramClient, events

API_ID = "28418618"
API_HASH = "993aded4010f0bdf844dc777859516b8"
BOT_TOKEN = "7611699084:AAErPfRjOMYJVY7kfzlFkazXNyi8SwiKB4c"

client = TelegramClient("P1bot_session", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(pattern=r"/calc (.+)"))
async def message_handler(event):
    try:
        user_input = event.pattern_match.group(1)

        result = eval(user_input)
        await event.reply(f"result : {result}")
        
    except:
        await event.reply("خطا در کد داریم.")

print("Bot is running ...")
client.run_until_disconnected()