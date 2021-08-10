import requests
import os
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from youtube_dl import YoutubeDL

API_ID = os.environ.get('APP_ID')
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('TOKEN')

bot = Client('bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)

@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I am a bot to download persian subs from worldsubtitle website, just send me a movie name")

@bot.on_message(filters.private)
async def subdl(bot, message):
    REQ = requests.get(f"https://worldsubtitle.site/movies/{message.text}")
    try:
        LINK = BeautifulSoup(REQ, 'html.parser').find_all('a')
        print(LINK)
        await message.reply(f"{LINK}")
    except Exception as e:
        print(e)
        await message.reply("Sorry i cant find it plz choose number of these")

bot.run()
