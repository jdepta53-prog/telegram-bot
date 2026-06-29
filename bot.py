from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8839688187:AAHLG4JH8pJagBz-D_5X3E2kzsaPDVLas-Q"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot działa!")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot uruchomiony...")
app.run_polling()
