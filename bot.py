import telebot
from config import BOT_TOKEN, OWNER_ID

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda m: True)
def forward_to_owner(message):
    try:
        bot.forward_message(OWNER_ID, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "درخواست شما دریافت شد و در صف بررسی قرار گرفت.")
    except Exception as e:
        bot.send_message(message.chat.id, "خطایی رخ داد. لطفاً دوباره تلاش کنید.")

bot.infinity_polling()