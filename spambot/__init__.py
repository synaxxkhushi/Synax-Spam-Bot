import asyncio
import logging
from telethon import TelegramClient
from spambot.config import Config
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN1 = Config.BOT_TOKEN1
BOT_TOKEN2 = Config.BOT_TOKEN2
BOT_TOKEN3 = Config.BOT_TOKEN3
BOT_TOKEN4 = Config.BOT_TOKEN4
BOT_TOKEN5 = Config.BOT_TOKEN5
OWNER_ID = Config.OWNER_ID
OWNER_NAME = str(Config.OWNER_NAME) if Config.OWNER_NAME else "MafiaSpamBot"
OWNER_USERNAME = str(Config.OWNER_USERNAME) if Config.OWNER_USERNAME else "MafiaBot_Support"
CO_OWNER_ID = Config.CO_OWNER_ID
SUDO_USERS = Config.SUDO_USERS
DISPLAY_PIC = str(Config.DISPLAY_PIC) if Config.DISPLAY_PIC else "https://telegra.ph/file/0db6ef22ae3b481c3891c.jpg"
BIO_MSG = str(Config.BIO_MSG) if Config.BIO_MSG else "Mafia Spam Bot Ready To Fuck Haters!"
HEROKU_API_KEY = Config.HEROKU_API_KEY
HEROKU_APP_NAME = Config.HEROKU_APP_NAME

BOT_VERSION = 1.0

GOD_USERS = [1212368262]
DEV_USERS = [1212368262]
MY_USERS = [1212368262]
LIMIT = [1212368262]

MY_USERS.append(OWNER_ID)
MY_USERS.extend(CO_OWNER_ID)
MY_USERS.extend(SUDO_USERS)

LIMIT.append(OWNER_ID)
LIMIT.extend(CO_OWNER_ID)

GOD_USERS.append(OWNER_ID)

async def main():
    global MafiaBot1
    global MafiaBot2
    global MafiaBot3
    global MafiaBot4
    global MafiaBot5

    if BOT_TOKEN1:
        print("Working On Bot Token 1!")
        try:
            MafiaBot1 = TelegramClient("MafiaSpamBot1", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 1 OK!")
            await MafiaBot1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 1 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "MafiaSpamBot1"
            MafiaBot1 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await MafiaBot1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            pass

    if BOT_TOKEN2:
        print("Working On Bot Token 2!")
        try:
            MafiaBot2 = TelegramClient("MafiaSpamBot2", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 2 OK!")
            await MafiaBot2.start(bot_token=BOT_TOKEN2)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 2 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "MafiaSpamBot2"
            MafiaBot2 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await MafiaBot2.start(bot_token=BOT_TOKEN2)
        except Exception as e:
            pass
    
    if BOT_TOKEN3:
        print("Working On Bot Token 3!")
        try:
            MafiaBot3 = TelegramClient("MafiaSpamBot3", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 3 OK!")
            await MafiaBot3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 3 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "MafiaSpamBot3"
            MafiaBot3 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await MafiaBot3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            pass

    if BOT_TOKEN4:
        print("Working On Bot Token 4!")
        try:
            MafiaBot4 = TelegramClient("MafiaSpamBot4", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 4 OK!")
            await MafiaBot4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 4 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "MafiaSpamBot4"
            MafiaBot4 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await MafiaBot4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            pass
    
    if BOT_TOKEN5:
        print("Working On Bot Token 5!")
        try:
            MafiaBot5 = TelegramClient("MafiaSpamBot5", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 5 OK!")
            await MafiaBot5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 5 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "MafiaSpamBot5"
            MafiaBot5 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await MafiaBot5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            pass

            
loop = asyncio.get_event_loop()

loop.run_until_complete(main())
