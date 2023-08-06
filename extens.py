import requests
import json
from config import keys

class Apiexeption(Exception):
    pass
class Rateconverter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise Apiexeption(f'Не удалось найти валюту {quote}.')
        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise Apiexeption(f'Не уадлось найти валюту {base}.')
        try:
            if quote_ticker == base_ticker:
                raise (f'Невозможно конвертировать одинаковые валюты{base}')
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise Apiexeption(f'Не удалось обработать колличество {amount}.')

        r = requests.get(f"https://api.coingate.com/v2/rates/merchant/{base_ticker}/{quote_ticker}")
        resp = json.loads(r.content)
        new_price = resp * float(amount)
        #new_price = round(new_price, 4)
        massege = f"Цена {amount} {keys[base]} в {keys[quote]} -->  {new_price}"
        return massege
