import os, math
from pyrogram import Client, filters

API_HASH = os.environ['API_HASH'] # Api hash
APP_ID = int(os.environ['APP_ID']) # Api id/App id
BOT_TOKEN = os.environ['BOT_TOKEN'] # Bot token


# Running bot
xbot = Client(
    'PersianSubBot',
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


START_MSG = """
سلام؛
به ربات جستجوگر و دانلودر زیرنویس فارسی‌ خوش آمدید.

اسم یک فیلم رو به روش زیر بفرستید:

A Savage Nature 2020

Fast And Furious 9 2021

نکته:
حروف اول کلمات را بزرگ بنویسید.
"""

@xbot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG)

@xbot.on_message(filters.text & filters.private)
async def loader(bot, message):
    m = message.text
    if ' ' in m:
        l = m.split(' ')
        if len(l) == 2:
            Y = m.split(None, 1)[1]
        elif len(l) == 3:
            Y = m.split(None, 2)[2]
        elif len(l) == 4:
            Y = m.split(None, 3)[3]
        elif len(l) == 5:
            Y = m.split(None, 4)[4]
        elif len(l) == 6:
            Y = m.split(None, 5)[5]
        elif len(l) == 7:
            Y = m.split(None, 6)[6]
        elif len(l) == 8:
            Y = m.split(None, 7)[7]
        elif len(l) == 9:
            Y = m.split(None, 8)[8]
    else:
        await message.reply("فک کنم سال ساخت فیلم رو وارد نکردی")
    if "And" or "Of" or "The" in m:
        if m.startswith("And") or m.startswith("Of") or m.startswith("The"):
            N = message.text.replace(" ", ".").message.text.replace("And", "and").message.text.replace("Of", "of").message.text.replace("The", "the") 
    else:
        N = message.text.replace(" ", ".")
    link = f"https://dl.worldsubtitle.site/wrpink/Movies/{Y}/{N}_WorldSubtitle.zip"
    await message.reply(link)
    


xbot.run()
