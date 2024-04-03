from spambot import *
from spambot import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5
from spambot.helpers.commands import *
from telethon import events, Button


Buttons = [
    Button.inline("ᴀʟɪᴠᴇ 🌹", b'alive'),
    Button.inline("ᴘɪɴɢ 🌹", b'ping')
], [
    Button.inline("ʀᴀɪᴅ 🌿", b'raid'),
    Button.inline("ʀᴇᴘʟʏ ʀᴀɪᴅ 🌿", b'replyraid')
], [
    Button.inline("sᴘᴀᴍ 🍀", b'spam'),
    Button.inline("ᴘsᴘᴀᴍ 🍀", b'pspam')
], [
    Button.inline("ᴇxᴛʀᴀs 🍁", b'extras'),
    Button.inline("ʜᴇʀᴏᴋᴜ 🍁", b'heroku')
], [
    Button.url("ᴄʜᴀɴɴᴇʟ 🍃", "t.me/synaxnetwork"),
    Button.url("ɢʀᴏᴜᴘ 🍃", "t.me/synaxchatgroup")
]

BACK = [
    Button.inline("Back", b'back')
]

@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(e):
    if e.sender_id in MY_USERS:
        message = await e.client.send_file(e.chat_id, DISPLAY_PIC, caption="This Is Help Command!!!", buttons=Buttons)

        

