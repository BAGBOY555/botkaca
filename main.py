from os.path import join as os_path_join
from pyrogram import Client, Message, MessageHandler, Filters, CallbackQueryHandler
from bot import CONFIG, COMMAND, LOCAL, LOGGER, STATUS
from bot.handlers import *
import asyncio

# Initialize bot
app = Client(
    "Bot",
    bot_token=CONFIG.BOT_TOKEN,
    api_id=CONFIG.API_ID,
    api_hash=CONFIG.API_HASH,
    workdir=os_path_join(CONFIG.ROOT, CONFIG.WORKDIR),
    plugins=dict(root="bot/handlers")
)
app.set_parse_mode("html")
