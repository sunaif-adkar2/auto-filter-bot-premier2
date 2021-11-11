# (c) @SpEcHIDe
# (c) @AlbertEinsteinTG
# (e) @sunaif_adkar
# Copyright permission under MIT License
# All rights reserved by Sunaif adkar
# change names if your edit this dont be over smart  Hutts your repository 

from pyrogram import Client, __version__

from . import API_HASH, APP_ID, LOGGER, BOT_TOKEN 

from .User import User

class SaBots(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "SaBots/Plugins"
            },
            workers=200,
            bot_token=BOT_TOKEN,
            sleep_threshold=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{bot_details.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
