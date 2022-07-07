import telebot
import config
import extensions

TOKEN = config.MY_TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    bot.reply_to(message, "Этот бот конвертирует заданное количество "
                          "одной валюты в соответствующее количество "
                          "другой валюты по текущему курсу. "
                          "Для вывода списка доступных валют введите "
                          "команду /values \n"
                          "Для получения результата расчета введите (в именительном "
                          "падеже в единственном числе) наименование валюты, "
                          "которую требуется купить, затем наименование валюты, "
                          "которую Вам не жалко, затем сумму первой валюты, "
                          "которую Вам требуется приобрести. ")

@bot.message_handler(commands=['values'])
def handle_val(message):
    bot.reply_to(message, "доллар \nевро \nйена \nрубль")

@bot.message_handler(content_types=['text'])
def function_name(message):
    list_ = message.text.split()
    try:
        if len(list_) != 3:
            raise extensions.API_Exceptions_Number

        if list_[0] not in ['доллар', 'евро', 'рубль', 'йена'] or list_[1] not in ['доллар', 'евро', 'рубль', 'йена']:
            raise extensions.API_Exceptions_Val

        if not int(list_[2]):
            raise extensions.API_Exceptions_Digit

    except extensions.API_Exceptions_Number:
        bot.reply_to(message, "Вы ввели не три параметра! "
                              "\nПовторите ввод по правилу: \nВалюта№1  Валюта№2  СуммаВалюта№1")
    except extensions.API_Exceptions_Val:
        bot.reply_to(message, "Вы ввели неправильное наименование валюты! "
                              "\nПовторите ввод по правилу: \nВалюта№1  Валюта№2  СуммаВалюта№1")
    except extensions.API_Exceptions_Digit:
        bot.reply_to(message, "Вы ввели неверное число! "
                              "\nПовторите ввод по правилу: \nВалюта№1 Валюта№2 СуммаВалюта№1.")
    else:
        base = list_[0]
        quote = list_[1]
        quantity = list_[2]
        bot.reply_to(message, extensions.Get_price.get_price(base, quote, quantity))

bot.polling(none_stop=True)
