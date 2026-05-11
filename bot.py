from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes
import os

BOT_TOKEN = os.getenv("8761988573:AAFZzj7nnsooeg89kNAIF_OXR7ROs_DTOK0")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Advanced OSINT Bot Running ✅"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("BOT RUNNING")

app.run_polling()
