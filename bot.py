from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

ADMIN_ID = int(os.getenv("raketa_kirill"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет 👋\nОставь свой отзыв о магазине ЦентроMania. Просто напиши его в чат!"
    )

async def handle_review(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    await update.message.reply_text("Спасибо за отзыв! Мы его обязательно учтём 🙌")

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📩 Новый отзыв от @{user.username or user.first_name}:\n\n{text}"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_review))

    print("Бот запущен...")
    app.run_polling()
