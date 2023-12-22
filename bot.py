
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio
from datetime import datetime
import pytz

Bot = Client(
    name = "membercountermeta",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)
app = Bot()
app.run()
