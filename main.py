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
                "گزینه اول",
                text = "1 متن تست"
            ),
            builder.article(
                "گزینه دوم",
                text = "2 متن تست"
            )
        ]

        await event.answer(inline_items, cache_time=0)

print("bot is running...")
client.run_until_disconnected()