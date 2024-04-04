from spambot import *
from spambot import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5
from telethon import events, Button


data  = [
    Button.url("sᴜᴘᴘᴏʀᴛ", url="t.me/synaxchatgroup"),
    Button.url("ᴏᴡɴᴇʀ", url="t.me/Coder_s4nax"),
    Button.url("ᴜᴘᴅᴀᴛᴇ", url="t.me/synaxnetwork")
]


@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[ 🧸 sʏɴᴀx ❤️](tg://user?id={6231550362})"
        sudo_user = ""
        if e.sender_id in MY_USERS:
            sudo_user = "True"
        else:
            sudo_user = "False"
        ON_START = f"""
ʜᴇʏ ʙᴀʙʏ 🙊 {mention},

♡ ᴛʜɪs ɪs sʏɴᴀx sᴘᴀᴍ ʙᴏᴛ ♡

ღ ɪᴛs ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟ sᴘᴀᴍʙᴏᴛ ᴅᴏɴ'ᴛ ᴍɪssᴜsᴇ ღ

🌷 ᴏᴡɴᴇʀ :- {myOwner}

sᴜᴅᴏ 🌱:- {sudo_user}

🇮🇳 ᴅᴇᴠᴇʟᴏᴘᴇʀ :- {creator}
    """
        await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=ON_START, buttons=data)

