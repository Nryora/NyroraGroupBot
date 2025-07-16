import telebot

# ✅ ضع توكن البوت هنا
TOKEN = 'ضع_توكن_البوت_هنا'

bot = telebot.TeleBot(TOKEN)

# ✅ ترحيب تلقائي بالأعضاء الجدد في المجموعات فقط
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for user in message.new_chat_members:
        bot.send_message(
            message.chat.id,
            f"✨ أهلاً وسهلاً {user.first_name}! 🫀 نورت المجموعة ✨"
        )

# ✅ تشغيل البوت
bot.infinity_polling()
