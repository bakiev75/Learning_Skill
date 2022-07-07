"""
1. Класс со статическим методом get_price отправки API-запросов. Принимает три аргумента и возвращает сумму в валюте.

2. Классы собственных исключений API_Exception_ХХХ для отлавливания ошибки пользователя и возврата сообщения пользователю.
"""

import requests
import json

class Get_price:
    @staticmethod
    def get_price(base, quote, quantity):
        data_html = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')      # Запрос API
        data = json.loads(data_html.content)                                        # Перевод в словарь с помощью JSON

        usd = data['Valute']['USD']['Value'] / data['Valute']['USD']['Nominal']
        usd_name = data['Valute']['USD']['CharCode']

        eur = data['Valute']['EUR']['Value'] / data['Valute']['EUR']['Nominal']
        eur_name = data['Valute']['EUR']['CharCode']

        jpy = data['Valute']['JPY']['Value'] / data['Valute']['JPY']['Nominal']
        jpy_name = data['Valute']['JPY']['CharCode']

        values_dir = {'доллар': usd, 'евро': eur, 'йена': jpy, 'рубль': 1}
        values_name = {'доллар': usd_name, 'евро': eur_name, 'йена': jpy_name, 'рубль': 'RUB'}

        result = (values_dir.get(base)/ values_dir.get(quote)) * float(quantity)

        return f"Для покупки {quantity} {values_name.get(base)} Вам необходимо {round(result, 4)} {values_name.get(quote)}"

class API_Exceptions_Number(Exception):             # Вызывается, если пользоваль ввел меньше или больше трёх пераметров
    pass

class API_Exceptions_Val(Exception):                # Вызывается, если пользователь ввел валюту с ошибкой или не из списка
    pass

class API_Exceptions_Digit(Exception):              # Вызывается, если пользователь ввел не число
    pass

if __name__ == '__main__':                                  # Для проверки работоспособности данного модуля в автономном режиме
    print(Get_price.get_price('доллар', 'рубль', '100'))
