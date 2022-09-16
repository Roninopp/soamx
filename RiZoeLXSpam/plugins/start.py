import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, ALIVE_PIC

RIZ_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"


Riz_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/RiZoeLX"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/DNHxHELL")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/MrRizoel/RiZoeLXSpam")
        ]
        ]


@Riz.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝐑𝐈𝐙𝐎𝐄𝐋 𝐗](https://t.me/RiZoeLX)**"
       await Riz.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)
                
