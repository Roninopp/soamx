from .. import Riz, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
    
HELP_PIC = "https://telegra.ph/file/71368798b617ea51ed005.jpg"

Riz_Help = "๐ฅ ๐ฅ๐ข๐ก๐๐ก ๐ซ ๐ฆ๐ฃ๐๐  ๐ฅ\n\n"
 
Riz_Help += f"__แดแดแดs แดแด แดษชสแดสสแด ษชษด ๐ฟ๐ผ๐ป๐ถ๐ป x sแดแดแด__\n\n"

Riz_Help += f" โง ๐๐๐ด๐๐ฑ๐พ๐ ๐ฒ๐ผ๐ณ๐ โง\n\n"

Riz_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots\n\n"
 
Riz_Help += f" โง ๐ป๐ด๐ฐ๐๐ด ๐ฒ๐ผ๐ณ โง\n\n"

Riz_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
Riz_Help += f" โง ๐๐ฟ๐ฐ๐ผ ๐ฒ๐ผ๐ณ๐ โง\n\n"

Riz_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n\n"
 
Riz_Help += f"แดสษชแดแด สแดสแดแดก สแดแดแดแดษด าแดส แดแดสแด ษชษดาแด.\n\n"

Riz_Help += f"ยฉ @DushmanXRonin | @DushmanXRonin\n"


@Riz.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
        [
        Button.url("แดสส แดแดแดs", "https://telegra.ph/file/71368798b617ea51ed005.jpg7%A0-11-28-2")
        ],
        [
        Button.url("๐๐ผโ๐ธ โ๐ธโ๐ธ", "https://t.me/Dushmanxronin")
        ] 
        ]
        )                                                         
