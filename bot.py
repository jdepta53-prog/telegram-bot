from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "TU_WKLEJ_TOKEN_Z_BOTFATHER"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cześć! Bot działa! 🤖")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot uruchomiony...")
    app.run_polling()

if __name__ == "__main__":
    main()"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cześć! Bot działa! 🤖")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot uruchomiony...")
    app.run_polling()

if __name__ == "__main__":
    main()
