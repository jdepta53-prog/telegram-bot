from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8839688187:AAFX-hg0oqqiDw3u3oaYHv4yI7A832XO8Co"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cześć! Bot działa 🤖")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot uruchomiony...")
app.run_polling()
