#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [MemberCounterMeta Telegram bot by TeLe TiPs] (https://github.com/teletips/DATE_TIME_USERBOT-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/MemberCounterMeta

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio
from datetime import datetime
import pytz
from texts.texts_teletips import *


CHANNEL_OR_GROUP_LIST = [i.strip() for i in os.environ.get("CHANNEL_OR_GROUP_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])

TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
BOT_CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
BOT_MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

print(text_1)
async def main_MemberCounterMeta():
    async with MemberCounterMeta:
        try:
            while True:
                print(text_2)
                edit_message_text_teletips = "**📈 | Real-Time Member Counter** [Powered By Nihar](t.me/ryuk_xy)"
                
                for CHANNEL_OR_GROUP in CHANNEL_OR_GROUP_LIST:
                    try:
                        desired_timezone = 'Asia/Kolkata'
                        current_time = datetime.now(pytz.timezone(desired_timezone)).strftime("%Y-%m-%d %H:%M:%S")
                        get_chat_teletips = await MemberCounterMeta.get_chat(int(CHANNEL_OR_GROUP))   
                        if get_chat_teletips.type == "channel":
                            edit_message_text_teletips += f"\n\n📣  **{get_chat_teletips.title} 📊**\n👤 ├ <i>{get_chat_teletips.members_count} Subscribers</i>\n🔗 └ <i>[Link]({get_chat_teletips.invite_link})</i>"
                        else:
                            edit_message_text_teletips += f"\n\n💬  **{get_chat_teletips.title} 📊**\n👤 ├ <i>{get_chat_teletips.members_count} Members</i>\n🔗 └ <i>[Link]({get_chat_teletips.invite_link})</i>" 
                        await asyncio.sleep(2)
                    except ValueError:
                        print(f'ID not found: {CHANNEL_OR_GROUP }. Skipping...')                       
                edit_message_text_teletips += f"\n\n<i>🌀 Automatically refreshes every 15 minutes \n\n ♻️ **Last Refreshed** : {current_time} ({desired_timezone}) </i>"
                try:
                    await MemberCounterMeta.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, edit_message_text_teletips, disable_web_page_preview=True)
                except Exception:
                    pass    
                print(text_3)              
                await asyncio.sleep(900) # 15 minutes = 900 seconds
        except FloodWait as e:
            await asyncio.sleep(e.x)



  

MemberCounterMeta.run(main_MemberCounterMeta())

#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
