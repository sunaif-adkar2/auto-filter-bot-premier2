# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG
# (e) @sunaif adkar
# Copyright permission under MIT License
# All rights reserved by Sunaif Adkar
# change only name if your edit thus repo donr be over smart 🤓
import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .Translation import Translation

# Change Accordingly While Deploying To A VPS
# API_ID From https://my.telegram.org
APP_ID = int(os.environ.get("APP_ID"))
# API_HASH From https://my.telegram.org
API_HASH = os.environ.get("API_HASH")
# BOT_TOKEN From https://t.me/BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# DD_URI From https://www.mongodb.com/
DB_URI = os.environ.get("DB_URI")
# USER_SESSION From https://replit.com/@prgofficial/String-Gen
USER_SESSION = os.environ.get("USER_SESSION")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
