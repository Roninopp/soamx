from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/71368798b617ea51ed005.jpg"
  

          
rizoel = "✧ 𝙈𝘼𝘼 𝘾𝙃𝙊𝘿𝙉𝙀 𝙆𝙀 𝙇𝙄𝙔𝙀 𝙍𝙀𝘼𝘿𝙔 𝙃𝙐 ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **Roninbot ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Ronin_Sanki_fighters"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/RoninXJin_updates")
        ],
        [
        Button.url("• 𝕄𝔼ℝ𝔸 ℙ𝔸ℙ𝔸•", "https://t.me/DushmanXRonin")
        ]
        ]
        )
    
