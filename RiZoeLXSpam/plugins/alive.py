from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/71368798b617ea51ed005.jpg"
  

          
rizoel = "β§ ππΌπΌ πΎπππΏππ ππ ππππ πππΌπΏπ ππ β§\n\n"

rizoel += f"ββββββββββββββββββββ\n"

rizoel += f"β£β£ **α΄Κα΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `3.9.6`\n"

rizoel += f"β£β£ **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `{version.__version__}`\n"

rizoel += f"β£β£ **Roninbot α΄ α΄ΚsΙͺα΄Ι΄**  : `{rizoelversion}`\n"

rizoel += f"ββββββββββββββββββββ\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("α΄Κα΄Ι΄Ι΄α΄Κ", "https://t.me/Ronin_Sanki_fighters"),
        Button.url("sα΄α΄α΄α΄Κα΄", "https://t.me/RoninXJin_updates")
        ],
        [
        Button.url("β’ ππΌβπΈ βπΈβπΈβ’", "https://t.me/DushmanXRonin")
        ]
        ]
        )
    
