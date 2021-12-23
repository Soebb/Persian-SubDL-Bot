import os
import requests
from pyrogram import Client, filters

API_HASH = os.environ['API_HASH'] # Api hash
API_ID = os.environ['API_ID'] # Api id/App id
BOT_TOKEN = os.environ['BOT_TOKEN'] # Bot token

dirs = 'dl/'


# Running bot
xbot = Client(
    'PersianSubBot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


START_MSG = """
سلام؛
به ربات جستجوگر و دانلودر زیرنویس فارسی‌ خوش آمدید.

اسم یک فیلم رو به روش زیر بفرستید:

A Savage Nature 2020

Fast And Furious 9 2021
"""


@xbot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG)


@xbot.on_message(filters.private & filters.text & ~filters.regex('/start'))
async def subdl(bot, message):

    if not os.path.isdir(dirs):
        os.makedirs(dirs)

    year = message.text.split()[-1]
    if not year or (not year.__contains__("20") and not year.__contains__("19")):
        return await message.reply("سال ساخت فیلم رو وارد نکردی")

    splited = message.text.split()[:-1]
    title = ''
    for i in range(len(splited)):
        s = splited[-1+i]
        title += s[:1].upper() + s[1:len(s)].lower() + '.'

    if not title.startswith(("And", "Of", "The", "With")):
        title = title.replace("And", "and").replace("Of", "of").replace("With", "with").replace("The", "the") 

    link = f"https://dl.worldsubtitle.site/wrpink/Movies/{year}/{title}{year}_WorldSubtitle.zip"
    r = requests.get(link, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
    dldir = f'{dirs}{title}zip'
    if r.status_code == 200:
        f = open(dldir, 'wb')
        f.write(r.content)
        f.close
        await message.reply_document(document=dldir, caption=f"{message.text} زیرنویس فارسی فیلم")
    else:
        await message.reply("متاسفانه چنین زیرنویسی در سایت موجود نیست")


xbot.run()
