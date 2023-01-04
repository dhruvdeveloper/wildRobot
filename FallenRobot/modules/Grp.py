import random

import asyncio

from pyrogram import filters

from FallenRobot import pbot as FallenRobot

GRP_STRINGS = [

    "ABOUT MY CHANNELS AND GROUP CHATS......... MY SUPPORT GROUP : @GFC_SUPPORT , GFC CHANNEL : @GFC_COMMUNITY , GROUP CHAT : @VIRTUAL_ADDA "

]

@FallenRobot.on_message(filters.command("NETWORKS"))

async def lel(bot, message):

    ran = random.choice(ABOUTOWNER_STRINGS)

    await bot.send_chat_action(message.chat.id, "typing")

    await asyncio.sleep(1.5)

    return await message.reply_text(text=ran)

__mod_name__ = "NETWORKS"

__help__ = """

ABOUT NETWORKS .

❍ /networks *:* ABOUT BOT NETWORKS

 """
