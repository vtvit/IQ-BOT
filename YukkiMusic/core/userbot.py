#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"دەسپێکردنی یاریدەدەری کڕیارەکان")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("IQaizen")
                await self.one.join_chat("IQerenh")
                await self.one.join_chat("xv7amo")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, "یاریدەدەر دەستیپێکرد"
                )
            except:
                LOGGER(__name__).error(
                    f"ئەکاونتی یاریدەدەری 1 سەرکەوتوو نەبوو لە چوونە ژورەوەی گرووپی تۆمار. دڵنیابە لەوەی کە تۆ یاریدەدەرەکەت زیاد کردووە بۆ گروپی تۆمارەکەت و بەرز کراوەتەوە وەک بەڕێوەبەر! "
                )
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"یاریدەدەر دەستی پێکرد  {self.one.name}"
            )
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("IQaizen")
                await self.two.join_chat("IQerenh")
                await self.two.join_chat("xv7amo")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, "یاریدەدەر دەستی پێکرد"
                )
            except:
                LOGGER(__name__).error(
                    f"ئەکاونتی یاریدەدەری 2 سەرکەوتوو نەبوو لە چوونە ژورەوەی گرووپی تۆمار. دڵنیابە لەوەی کە تۆ یاریدەدەرەکەت زیاد کردووە بۆ گروپی تۆمارەکەت و بەرز کراوەتەوە وەک بەڕێوەبەر! "
                )
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            LOGGER(__name__).info(
                f"یاریدەدەری دوو دەستی پێکرد {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("TeamYukki")
                await self.three.join_chat("TheYukki")
                await self.three.join_chat("YukkiSupport")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, "یاریدەدەر دەستی پێکرد"
                )
            except:
                LOGGER(__name__).error(
                    f"ئەکاونتی یاریدەدەری 3 سەرکەوتوو نەبوو لە چوونە ژورەوەی گرووپی تۆمار. دڵنیابە لەوەی کە تۆ یاریدەدەرەکەت زیاد کردووە بۆ گروپی تۆمارەکەت و بەرز کراوەتەوە وەک بەڕێوەبەر! "
                )
                sys.exit()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            LOGGER(__name__).info(
                f"یاریدەدەری سێ دەستی پێکرد {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("IQaizen")
                await self.four.join_chat("IQerenh")
                await self.four.join_chat("xv7amo")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, "یاردەدەر دەستی پێکرد"
                )
            except:
                LOGGER(__name__).error(
                    f"ئەکاونتی یاریدەدەری 4 سەرکەوتوو نەبوو لە چوونە ژورەوەی گرووپی تۆمار. دڵنیابە لەوەی کە تۆ یاریدەدەرەکەت زیاد کردووە بۆ گروپی تۆمارەکەت و بەرز کراوەتەوە وەک بەڕێوەبەر! "
                )
                sys.exit()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            LOGGER(__name__).info(
                f"یاریدەدەری چوار دەستی پێکرد {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("IQaizen")
                await self.five.join_chat("IQerenh")
                await self.five.join_chat("xv7amo")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, "یاریدەدەر دەستی پێکرد"
                )
            except:
                LOGGER(__name__).error(
                    f"ئەکاونتی یاریدەدەر 5 سەرکەوتوو نەبوو لە چوونە ژورەوەی گرووپی تۆمار. دڵنیابە لەوەی کە تۆ یاریدەدەرەکەت زیاد کردووە بۆ گروپی تۆمارەکەت و بەرز کراوەتەوە وەک بەڕێوەبەر! "
                )
                sys.exit()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            LOGGER(__name__).info(
                f"یاریدەدەری پێنج دەستی پێکرد {self.five.name}"
            )
