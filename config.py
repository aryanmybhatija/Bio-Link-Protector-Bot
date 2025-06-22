# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

import os
import re
from dotenv import load_dotenv

# Load environment variables from a .env file (optional)
load_dotenv()

API_ID = os.getenv("API_ID")  # Your Telegram API ID
API_HASH = os.getenv("API_HASH")  # Your Telegram API Hash
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Your Bot Token

# MongoDB connection URI
MONGO_URI = os.getenv("MONGO_URI")

DEFAULT_WARNING_LIMIT = 3
DEFAULT_PUNISHMENT = "mute"  # Options: "mute", "ban"
DEFAULT_CONFIG = ("warn", DEFAULT_WARNING_LIMIT, DEFAULT_PUNISHMENT)

# Regex pattern to detect URLs in user bios
URL_PATTERN = re.compile(
    r'(https?://|www\.)[a-zA-Z0-9.\-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9._%+-]*)*'
)
