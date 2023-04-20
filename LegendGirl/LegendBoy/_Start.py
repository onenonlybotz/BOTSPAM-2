from LegendBS.start import start_cmd
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

from LegendGirl.Config import *

from ..core.clients import *

if START_MESSAGE:
    START_MESSAGE = START_MESSAGE
else:
    START_MESSAGE = (
        "This is a Powerful Bot Spam Made By [Baap Aaditya](https://t.me/Baap_Aaditya)"
    )


if START_PIC:
    START_PIC = START_PIC
else:
    START_PIC = "https://telegra.ph/file/5eb54b3b5c900b2fae835.jpg"


@Client.on_message(filters.command(["start"], prefixes=HANDLER))
async def _start(Legend: Client, message: Message):
    if ".jpg" in START_PIC or ".png" in START_PIC:
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_photo(
                    message.chat.id,
                    START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
                )
    elif ".mp4" in START_PIC.lower():
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_video(
                    message.chat.id,
                    START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
                )
    else:
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_message(
                    message.chat.id,
                    START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
                )
