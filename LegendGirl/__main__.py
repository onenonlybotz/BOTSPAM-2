import asyncio
import platform

from LegendBS.start_bot import start_bot
from pyrogram import __version__ as py_version
from pyrogram import idle

from . import *

loop = asyncio.get_event_loop()


async def Start_BotSpam():
    for i in range(1, 26):
        var = globals()[f"Client{i}"]
        if var is not None:
            await start_bot(var)
    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    print(f"🔥 Bot Spam 🔥[INFO] : Group Username {group_username}")
    print(f"🔥 Bot Spam 🔥[INFO] : Version - {platform.python_version()}")
    print(f"🔥 Bot Spam 🔥[INFO]: SpamBot Version - {version}")
    print(f"🔥 Bot Spam 🔥[INFO]: Pyrogram Version - {py_version}")
    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(Start_BotSpam())
    print(" Good Bye ! ")
