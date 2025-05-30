import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "22486555"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "312078a4f2a2a5186a91f41b7343cb00")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7815514686:AAF75oEabV0GBuE0LlzuFFzCrNH2-isE4j4")

OWNER_ID = int(os.environ.get("OWNER_ID", "7997003922"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "953685850").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://opz97167:opz97167@cluster0.mlxp6wz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002571982723"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002571982723")  # Optional here you'll get all logs
