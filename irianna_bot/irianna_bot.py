import telebot
import requests
import json
import config

data_html = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')

data = json.loads(data_html.content)

print(data)

usd = data['Valute']['USD']['Value'] / data['Valute']['USD']['Nominal']
usd_name = data['Valute']['USD']['CharCode']

eur = data['Valute']['EUR']['Value'] / data['Valute']['EUR']['Nominal']
eur_name = data['Valute']['EUR']['CharCode']

jpy = data['Valute']['JPY']['Value'] / data['Valute']['JPY']['Nominal']
jpy_name = data['Valute']['JPY']['CharCode']

rub = 1

values_dir = {'доллар':usd, 'евро':eur, 'йена':jpy, 'рубль':1}
values_name = {'доллар':usd_name, 'евро':eur_name, 'йена':jpy_name, 'рубль':'RUB'}

print(values_dir)

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
def handle_start(message):
    bot.reply_to(message, "доллар \nевро \nйена \nрубль")

@bot.message_handler(content_types=['text'])
def function_name(message):
    list_ = message.text.split()
    print((list_))
    a = float(values_dir.get(list_[0]))
    print(a)

    b = float(values_dir.get(list_[1]))
    print(b)

    c = float(list_[2])
    print(c)
    d = (a / b) * c

    bot.reply_to(message, round(d, 4))
    bot.send_message(message.chat.id, f"Для покупки {list_[2]} {values_name.get(list_[0])} "
                                      f"Вам необходимо {round(d, 4)} {values_name.get(list_[1])}")

bot.polling(none_stop=True)
