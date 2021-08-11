import os, time, math
import lk21
import requests
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
؛سلام
به ربات جستجوگر و دانلودر زیرنویس فارسی‌ خوش آمدید.

اسم یک فیلم رو به روش زیر بفرستید:

A savage nature 2020

Fast and furious 9 2021
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
    N = message.text.replace(" ", "-")
    link = f"https://dl.worldsubtitle.site/wrpink/Movies/{Y}/{N}_WorldSubtitle.zip"
    dirs = f'dl/'
    if not os.path.isdir(dirs):
        os.makedirs(dirs)
    dldir = f'{dirs}{N}.zip'
    bypasser = lk21.Bypass()
    url = bypasser.bypass_url(link)
    response = requests.get(link, stream=True)
    handle = open(dldir, "wb")
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:  # filter out keep-alive new chunks
            handle.write(chunk)
    handle.close()
    try:
        await message.reply_document(
            document=dldir,
            caption=f"{message.text}")
    except Exception as e:
        print(e)
        await message.reply("متاسفانه چنین زیرنویسی در سایت موجود نیست")
    


xbot.run()
