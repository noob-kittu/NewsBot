import requests
from telethon import TelegramClient
from telethon import events
import os
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = os.environ.get("APP_ID", default=None)
API_HASH = os.environ.get("API_HASH", default=None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", default=None)


bot = TelegramClient("NewsBot", APP_ID, API_HASH)
start = bot.start(bot_token=BOT_TOKEN) 



@bot.on(events.NewMessage(pattern="^/start"))
async def _(event):
    await event.reply('''Hello this is news bot made by Kittu. \n you can get live daily news via this bot. \n just hit command - \n /news \n /news bollywood \n it will send you all news in bot DM. ''')



@bot.on(events.NewMessage(pattern="^/news ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
       await event.reply('Currently This Module Only Works in my [PM](tg://user?id=1624337697)')
       return
    else:
       pass
    infintyvar = event.pattern_match.group(1)
    main_url = f"https://inshortsapi.vercel.app/news?category={infintyvar}"
    stuber = await event.reply(
        f"Ok ! Fectching {infintyvar} From inshortsapi Server And Sending To News Channel",
    )
    await stuber.edit("All News Has Been Sucessfully fetched, sendning to you.")
    starknews = requests.get(main_url).json()
    for item in starknews["data"]:
        sedlyf = item["content"]
        img = item["imageUrl"]
        writter = item["author"]
        dateis = item["date"]
        readthis = item["readMoreUrl"]
        titles = item["title"]
        sed1 = img
        sedm = f"**Title : {titles}** \n{sedlyf} \nDate : {dateis} \nAuthor : {writter} \nReadMore : {readthis}"
        await bot.send_file(event.chat_id, sed1, caption=sedm)





print ("Successfully Started")
start.run_until_disconnected()