import os, lk21, time, requests, math
from urllib.parse import unquote
from pySmartDL import SmartDL
from urllib.error import HTTPError
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image

# Configs
API_HASH = os.environ['API_HASH'] # Api hash
APP_ID = int(os.environ['APP_ID']) # Api id/App id
BOT_TOKEN = os.environ['BOT_TOKEN'] # Bot token


# https://github.com/viperadnan-git/google-drive-telegram-bot/blob/main/bot/helpers/downloader.py
def download_file(url, dl_path):
  try:
    dl = SmartDL(url, dl_path, progress_bar=False)
    dl.start()
    filename = dl.get_dest()
    if '+' in filename:
          xfile = filename.replace('+', ' ')
          filename2 = unquote(xfile)
    else:
        filename2 = unquote(filename)
    os.rename(filename, filename2)
    return True, filename2
  except HTTPError as error:
    return False, error


# Running bot
xbot = Client(
    'PersianSubBot',
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


START_MSG = """
سلام
من ربات جستجوگر و دانلودر زیرنویس فارسی‌ام
:اسم یک فیلم رو به شیوه ی زیر بفرستید
A savage nature 2020
Fast and furious 9 2021
"""

@xbot.on_message(filters.command('start') & filters.private)
async def start(bot, update):
    await message.reply(START_MSG)

@xbot.on_message(filters.text & filters.private)
async def loader(bot, message):
    dirs = './downloads/'
    if not os.path.isdir(dirs):
        os.mkdir(dirs)
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
        await message.reply("سال تولید اثر رو وارد نکردی")
    N = m.text.replace(" ", "-")
    link = f'https://dl.worldsubtitle.site/wrpink/Movies/{Y}/{N}_WorldSubtitle.zip'
    bypasser = lk21.Bypass()
    url = bypasser.bypass_url(link)
    dl_path = download_file(url, dirs)
    try:
        await message.reply_document(
            document=dl_path,
            quote=True)
        os.remove(dl_path)
    except:
        await message.reply("متاسفانه چنین زیرنویسی در سایت موجود نیست")
    


xbot.run()
