from pyrogram import *
from pyrogram.types import *

def start(client, message):
    message.reply_text("""**/search <hentai name> to search**\n MADE WITH 💖 By @Nafisfuad1""", parse_mode="markdown")
