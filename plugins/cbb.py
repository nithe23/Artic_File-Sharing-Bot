from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 Movie Channel :</b> <a href='https://t.me/Madness_Movie'>Movies Channel</a> \n<b>📝 Web Series :</b> <a href='https://t.me/Series_Madness'>Series Madness</a> \n<b>📚 Chat Group:</b> <a href='https://t.me/Weebs/Madness'>Weebs Madness</a> \n<b>🚀 Ongoing Anime :</b> <a href='https://t.me/Ongoing_Madness'>Ongoing Anime</a> \n<b>📢 Channel :</b> <a href='https://t.me/Anime_Madness'>Anime Madness</a> \n<b>🧑‍💻 Developer :</b> <a href='tg://user?id={OWNER_ID}'>ŦrαfͥαlͣgͫαrŁαw</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
