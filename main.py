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
            [Button.text("دکمه اول", resize=True), Button.text("دکمه دوم", resize=True)],
            [Button.text("دکمه سوم", resize=True), Button.text("دکمه چهارم", resize=True)]
        ]
        await event.reply("اینم از دکمه هاتون جناب", buttons=keboard)

    if text == "دکمه دوم":
        await event.reply("فهمیدم دکمه دوم رو زدی")

    if text == "/dell":
        await event.reply("دکمه های شما با موفقیت حذف شد", buttons=Button.clear())
    

print("bot is running...")
client.run_until_disconnected()