import os
import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=TOKEN)

async def send_gold_price():
    message = "قیمت طلا امروز: به‌زودی..."
    await bot.send_message(chat_id=CHANNEL_ID, text=message)

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_gold_price, "cron", hour=11, minute=0)  # ارسال ساعت ۱۱ صبح
    scheduler.start()
    print("ربات روشن است...")
    while True:
        await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())
