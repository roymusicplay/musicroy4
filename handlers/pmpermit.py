from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hlo dear [π₯°](https://telegra.ph/file/f2c43863d300054125f22.jpg), This is a music assistant service .\n\n π Rules:\n   - No chatting allowed\n  - You will get non reply beacause it is a bot\n  - No spam allowed \n\n π **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n This Is very easy and comfortablein ise with 0% risk!!\n    - If you have any issue and doubt π§ just contact @KINGBOTOFFICIALCHAT.\n   - Thanks For Using β­ MUSICBOT β­ βΊοΈβΊοΈ\n\n")
  return
