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

MemberCounterMeta = Client(
    name = "membercountermeta",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)

CHANNEL_OR_GROUP_LIST = [i.strip() for i in os.environ.get("CHANNEL_OR_GROUP_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
BOT_CHANNEL_OR_GROUP_ID = int(os.environ["BOT_CHANNEL_OR_GROUP_ID"])
BOT_MESSAGE_ID = int(os.environ["BOT_MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]
C_MESSAGE_ID = int(os.environ["C_MESSAGE_ID"])



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
                edit_message_text_teletips += f"\n\n<i>🌀 Automatically refreshes every 45 minutes \n\n ♻️ **Last Refreshed** : {current_time} ({desired_timezone}) </i>"
                try:
                    await MemberCounterMeta.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, edit_message_text_teletips, disable_web_page_preview=True)
                except Exception:
                    pass    
                print(text_3)
                print("Checking...")
                xxx_teletips = f"📈 | **Real-Time Bot Status** Powered By Nihar"
                for bot in BOT_LIST:
                    try:
                        yyy_teletips = await MemberCounterMeta.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(10)
                        zzz_teletips = MemberCounterMeta.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_teletips:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n🌀  @{bot}\n        └ **Down** ❗️"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await MemberCounterMeta.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❗️")
                                except Exception:
                                    pass
                            await MemberCounterMeta.read_chat_history(bot)
                        else:
                            xxx_teletips += f"\n\n🌀  @{bot}\n        └ **Alive** ✅"
                            await MemberCounterMeta.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                
                # Countdown Logic
                time = datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%Y-%m-%d %H:%M:%S")
                xxx_teletips += f"\n\n⌛️ Last checked on: {last_update} ({TIME_ZONE})\n\n<i>♻️ Refreshes automatically Every 45 Minutues</i>"
                await MemberCounterMeta.edit_message_text(int(BOT_CHANNEL_OR_GROUP_ID), BOT_MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")
                await MemberCounterMeta.send_message(int(bot_admin_id), f"Last checked on: {last_update}")
                print(f"trying to do countdown")
                target_date = datetime(2023, 12, 31, 23, 59, 59)
                india_timezone = pytz.timezone('Asia/Kolkata')
                current_time_c = datetime.now(india_timezone)
                target_date = india_timezone.localize(target_date)
                remaining_time = target_date - current_time_c  # Use 'Asia/Kolkata' for Indian Standard Time
                if remaining_time.total_seconds() <= 0:
                    break
                days, seconds = divmod(remaining_time.seconds, 86400)
                hours, seconds = divmod(seconds, 3600)
                minutes, seconds = divmod(seconds, 60)
                countdown_message = (f"Countdown to December 31, 2023 (India Time):\n {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
                await MemberCounterMeta.edit_message_text(int(BOT_CHANNEL_OR_GROUP_ID), C_MESSAGE_ID, countdown_message)
                print(f"Countdown to December 31, 2023 (India Time):\n {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
                await asyncio.sleep(2700)  # 15 minutes = 900 seconds # 15 minutes = 900 seconds
        except FloodWait as e:
            await asyncio.sleep(e.x)
@MemberCounterMeta.on_message(filters.command("status", "!") & filters.me)
async def alive(_, message: Message):
    await message.edit("Your MemberCounter is alive!")
    await asyncio.sleep(10)
    await message.delete()               


MemberCounterMeta.run(main_MemberCounterMeta())
