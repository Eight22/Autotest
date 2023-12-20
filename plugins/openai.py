from info import SUPPORT_GROUP, SUPPORT_LINK, OPENAI_API
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from openai import OpenAI

ai_client = OpenAI(api_key=OPENAI_API)

@Client.on_message(filters.command("ask"))
async def ask_question(client, message):
    if len(OPENAI_API) == 0:
        return await message.reply("OPENAI_API is empty")
    try:
        text = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("Command Incomplete!\nUsage: /ask your_question")
    msg = await message.reply("Searching...")
    try:
        response = ai_client.chat.completions.create(
            messages=[
                {"role": "user", "content": text}
            ],
            model="gpt-3.5-turbo"
        )
        await msg.edit(f"💬 Query: <code>{text}</code>\n🦹 User: {message.from_user.mention}\n⚡ Results:\n<code>{response.choices[0].message.content}</code>")
    except Exception as e:
        await msg.edit(f'Error - <code>{e}</code>')
