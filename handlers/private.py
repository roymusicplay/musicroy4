from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgEAAx0CTEdZWQACC4VgtPsYrWBGcfDUYZ-2vJRG9dem-AACyQEAAh8UIERsZH-rbrIloh8E")
    await message.reply_text(
        f"""**Dear {message.from_user.first_name}!

😁 I am  Music Player. 

😅Currently you are using MUSIC PREMIUM VERSION! 😳

🥳 I can play music in your Telegram Group's Voice Chat😉

Developed by ⚡ @abhinasroy ⚡

My commands - type  /help to get commands, which work in grp

Thanks for using .

Regrards [KINGBOT](https://t.me/abhinasroy)
**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Father 🛠", url="https://t.me/abhinasroy")
                  ],[
                    InlineKeyboardButton(
                        "💬 Support Group", url="https://t.me/DOSTI_GROUP_1234"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/MOVIE_CHANNEL_1234"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/{}?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⭐MUSIC PLAYER IS ALWAYS ACTIVE!!⭐**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ Support⚡", url="https://t.me/DOSTI_GROUP_1234")
                ]
            ]
        )
   )
