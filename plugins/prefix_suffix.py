from pyrogram import Client, filters, enums
from helper.database import jishubotz


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Give The Prefix__\n\nExample:- `/set_prefix @Madflix_Bots`**")
    prefix = message.text.split(" ", 1)[1]
    JishuDeveloper = await message.reply_text("Please Wait ...")
    await jishubotz.set_prefix(message.from_user.id, prefix)
    await JishuDeveloper.edit("**Prefix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    JishuDeveloper = await message.reply_text("Please Wait ...")
    prefix = await jishubotz.get_prefix(message.from_user.id)
    if not prefix:
        return await JishuDeveloper.edit("**You Don't Have Any Prefix ❌**")
    await jishubotz.set_prefix(message.from_user.id, None)
    await JishuDeveloper.edit("**Prefix Deleted Successfully 🗑️**")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    JishuDeveloper = await message.reply_text("Please Wait ...")
    prefix = await jishubotz.get_prefix(message.from_user.id)
    if prefix:
        await JishuDeveloper.edit(f"**Your Prefix :-**\n\n`{prefix}`")
    else:
        await JishuDeveloper.edit("**You Don't Have Any Prefix ❌**")


# SUFFIX
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Give The Suffix__\n\nExample:- `/set_suffix @Madflix_Bots`**")
    suffix = message.text.split(" ", 1)[1]
    JishuDeveloper = await message.reply_text("Please Wait ...")
    await jishubotz.set_suffix(message.from_user.id, suffix)
    await JishuDeveloper.edit("**Suffix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    JishuDeveloper = await message.reply_text("Please Wait ...")
    suffix = await jishubotz.get_suffix(message.from_user.id)
    if not suffix:
        return await JishuDeveloper.edit("**You Don't Have Any Suffix ❌**")
    await jishubotz.set_suffix(message.from_user.id, None)
    await JishuDeveloper.edit("**Suffix Deleted Successfully ✅**")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_csuffix(client, message):

    JishuDeveloper = await message.reply_text("Please Wait ...")
    suffix = await jishubotz.get_suffix(message.from_user.id)
    if suffix:
        await JishuDeveloper.edit(f"**Your Suffix :-**\n\n`{suffix}`")
    else:
        await JishuDeveloper.edit("**You Don't Have Any Suffix ❌**")










# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
