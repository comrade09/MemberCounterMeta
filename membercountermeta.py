import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio
from datetime import datetime , timedelta
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
                edit_message_text_teletips = "**📈 | Real-Time Member Counter** "

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
                xxx_teletips = f"📈 | **Real-Time Bot Status** "
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
                                    await MemberCounterMeta.send_message(int(5496035221), f"🚨 **Beep! Beep!! @{bot} is down** ❗️")
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
                xxx_teletips += f"\n\n⌛️ Last checked on: {last_update} ({TIME_ZONE})\n\n<i>♻️ Refreshes automatically Every 45 Minutes</i>"
                await MemberCounterMeta.edit_message_text(int(BOT_CHANNEL_OR_GROUP_ID), BOT_MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")
                await MemberCounterMeta.send_message(int(5496035221), f"Last checked on: {last_update}")
                await asyncio.sleep(7)
                print(f"trying to do countdown")
                desired_timezone_c = 'Asia/Kolkata'
                target_date = datetime(2024, 5, 4, 23, 59, 59 , tzinfo=pytz.timezone(desired_timezone_c))
                current_time_c = datetime.now(pytz.timezone(desired_timezone_c))
                remaining_time = target_date - current_time_c  # Use 'Asia/Kolkata' for Indian Standard Time
               
                if remaining_time.total_seconds() <= 0:
                    print("Countdown reached zero.")
                else: 
                    total_seconds = remaining_time.total_seconds()
                    days, seconds_remaining = divmod(total_seconds, 86400)
                    hours, seconds_remaining = divmod(seconds_remaining, 3600)
                    minutes, seconds = divmod(seconds_remaining, 60)
                countdown_message = (f"🌀**COUNTDOWN FOR NEET 2024 to 5 May, 2024** \n\n **Time Left**: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds \n\n **Last Refreshed** : {current_time} ({desired_timezone}) \n\n <i>♻️ Refreshes automatically Every 45 Minutes </i>")
                await MemberCounterMeta.edit_message_text(int(BOT_CHANNEL_OR_GROUP_ID), C_MESSAGE_ID, countdown_message)
                print(f"COUNTDOWN FOR NEET 2024 to 5 May, 2024 \n\n Time Left: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds \n\n  ")
                await asyncio.sleep(2700)  # 15 minutes = 900 seconds # 15 minutes = 900 seconds
        except FloodWait as e:
            await asyncio.sleep(e.x)
@MemberCounterMeta.on_message(filters.command("status", "!") & filters.me)
async def alive(_, message: Message):
    await message.edit("Your MemberCounter is alive!")
    await asyncio.sleep(10)
    await message.delete()               


MemberCounterMeta.run(main_MemberCounterMeta())

