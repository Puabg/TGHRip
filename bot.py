import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from configparser import ConfigParser
from inline_keyboard import send_task_options, handle_callback
from access_control import is_authorized

config = ConfigParser()
config.read("config.ini")

TOKEN = config.get("TELEGRAM", "Token")
OWNER_ID = int(config.get("TELEGRAM", "OwnerID"))
AUTHORIZED_GROUP = int(config.get("TELEGRAM", "AuthorizedGroupID"))

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    if chat_id < 0 and chat_id != AUTHORIZED_GROUP:
        return

    if not is_authorized(user_id, chat_id):
        await update.message.reply_text("You are not authorized to use this bot.")
        return

    await update.message.reply_text("👋 Welcome to TGHRip!\nSend /rip <url> <key> to start ripping.")

async def rip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    if chat_id < 0 and chat_id != AUTHORIZED_GROUP:
        return

    if not is_authorized(user_id, chat_id):
        await update.message.reply_text("⛔ Not authorized.")
        return

    if len(context.args) < 2:
        await update.message.reply_text("Usage: /rip <url> <decryption_key>")
        return

    url, key = context.args[0], context.args[1]
    context.user_data['url'] = url
    context.user_data['key'] = key

    await send_task_options(update, context)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rip", rip))
    app.add_handler(CallbackQueryHandler(handle_callback))

    app.run_polling()
