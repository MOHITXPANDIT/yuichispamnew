from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/d93d6aea251fa5a738502.jpg"
  

          
rizoel = "✧ SPAM BOT IS ALIVE ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"
    
rizoel += f"┣➣ **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/NIGHT_FUN_XD)\n"

rizoel += f"┣➣ **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/AB0UTPANDIT)\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

rizoel += f"🖤 [𝐑𝐄𝐏𝐎](https://github.com/MOHITXPANDIT/yuichispamnew) 🖤"            
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
