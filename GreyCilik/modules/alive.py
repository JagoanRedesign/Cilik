import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from GreyCilik.events import register
from GreyCilik import telethn as tbot
from GreyCilik import BOT_USERNAME as bu

PHOTO = "https://telegra.ph/file/2a8514b5527d544e97545.jpg"

@register(pattern=("/alive"))
async def awake(event):
  GREY = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Cilik.** \n\n"
  GREY += "✪ **I'm Working Properly** \n\n"
  GREY += f"✪ **My Master : [𝓜𝓩 ᶜᵒᵈᵉʳ](https://t.me/mazekubot)** \n\n"
  GREY += f"✪ **Library Version :** `{telever}` \n\n"
  GREY += f"✪ **Telethon Version :** `{tlhver}` \n\n"
  GREY += f"✪ **Pyrogram Version :** `{pyrover}` \n\n"
  GREY += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", f"https://t.me/{bu}?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/Dutabotid")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=GREY,  buttons=BUTTON)
