import requests
from pyrogram import Client as Bot

from DEVIL-MUSIC.config import API_HASH
from DEVIL-MUSIC.config import API_ID
from DEVIL-MUSIC.config import BG_IMAGE
from DEVIL-MUSIC.config import BOT_TOKEN
from DEVIL-MUSIC.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="DEVIL-MUSIC.modules"),
)

bot.start()
run()
