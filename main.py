from telethon import TelegramClient, events

API_ID = 28418618
API_HASH = "993aded4010f0bdf844dc777859516b8"
BOT_TOKEN = "7611699084:AAErPfRjOMYJVY7kfzlFkazXNyi8SwiKB4c"

client = TelegramClient("bot_session", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.InlineQuery)
async def inline_mode(event):
    user_text = event.text.lower().strip()
    builder = event.builder

    if user_text == "test":
        inline_items = [
            builder.article(
                id =            "1", 
                title =         "گزینه اول", 
                description =   "این توضیحات گزینه اول است",
                url =           "https://t.me/SinaBanifazl", 
                text =          "پاسخ گزینه 1"
            ),
            builder.article(
                id =            "2", 
                title =         "گزینه دوم", 
                description =   "این توضیحات گزینه دوم است",
                url =           "https://instagram.com/SinaBanifazl", 
                text =          "پاسخ گزینه 2"
            )
        ]

        await event.answer(inline_items, cache_time=0)

print("bot is running...")
client.run_until_disconnected()