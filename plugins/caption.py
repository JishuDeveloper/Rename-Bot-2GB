from pyrogram import Client, filters 
from helper.database import jishubotz

@Client.on_message(filters.private & filters.command(['set_caption', "sc"]))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Give The Caption\n\nExample :- `/set_caption 📕Name ➠ : {filename} \n\n🔗 Size ➠ : {filesize} \n\n⏰ Duration ➠ : {duration}`**", quote=True)
    caption = message.text.split(" ", 1)[1]
    await jishubotz.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**Your Caption Successfully Added ✅**", quote=True)
   
@Client.on_message(filters.private & filters.command(['del_caption', "dc"]))
async def delete_caption(client, message):
    caption = await jishubotz.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**You Don't Have Any Caption ❌**", quote=True)
    await jishubotz.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**Your Caption Successfully Deleted 🗑️**", quote=True)
                                       
@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption', "vc"]))
async def see_caption(client, message):
    caption = await jishubotz.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Your Caption :**\n\n`{caption}`", quote=True)
    else:
       await message.reply_text("**You Don't Have Any Caption ❌**", quote=True)









# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @MadflixBotz
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
# Contact @MadflixSupport
