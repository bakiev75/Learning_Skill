import telebot

TOKEN = "5404764351:AAFMlTLshhMVNwA3zn7tDE41YquQabEpd-E"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f"Стартуем, {message.chat.username}!")


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "Помогаем")

@bot.message_handler(content_types=['document', 'audio', 'text'])
def function_name(message):
    bot.reply_to(message, "Сэр, Вы опять несете пургу!")

bot.polling(none_stop=True)
