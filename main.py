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
        keyboard = [
            [Button.text("دکمه اول", resize=True), Button.text("دکمه دوم", resize=True)],
            [Button.text("دکمه سوم", resize=True), Button.text("دکمه چهارم", resize=True)]
        ]
        await event.reply("اینم از دکمه هاتون جناب", buttons=keyboard)

    if text == "دکمه دوم":
        await event.reply("فهمیدم دکمه دوم رو زدی")

    if text == "/dell":
        await event.reply("دکمه های شما با موفقیت حذف شد", buttons=Button.clear())
    
    if text == "/inline":
        keyboard = [
            [Button.switch_inline(text="دکمه اینلاین", query="test")]
        ]
        await event.reply("دکمه حالت اینلاین", buttons=keyboard)

    if text == "/loc":
        keyboard = [
            [Button.request_location("ارسال لوکیشن", resize=True)]
        ]
        await event.reply("برای ارسال لوکیشن روی دکمه ارسال کلیک کنید", buttons=keyboard)

    if text == "/phone":
        keyboard = [
            [Button.request_phone("ارسال شماره تلفن", resize=True)]
        ]
        await event.reply("برای ارسال شماره تلفن روی دکمه ارسال کلیک کنید", buttons=keyboard)

    if text == "/smart":
        keyboard = [
            Button.inline(text= "کلیک کنید",
                          data= "banfao_3124")
        ]
        await event.reply("این دکمه شیشه ای شماست", buttons=keyboard)

    if text == "/url":
        keyboard = [
            Button.url(text= "برای ورود به گوگل کلیک کنید",
                    url= "https://www.google.com/")
        ]
        await event.reply("این دکمه شیشه ای شماست", buttons=keyboard)

@client.on(events.CallbackQuery(pattern=b"banfao_.*"))
async def call_back(event):
    user_id = int(event.data.decode().split("_")[1])
    await event.answer(f"{user_id}", alert=True)

print("bot is running...")
client.run_until_disconnected()