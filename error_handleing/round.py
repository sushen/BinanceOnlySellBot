import sys

sys.path.append("..")

from api_callling.api_calling import APICall

from main.all_variable import Variable


class PriceRound:

    def round_symbol_price(self, currency):
        currency_symbol = currency
        avg_price = APICall.client.get_avg_price(symbol=currency_symbol)
        amount_of_usd = Variable.DOLLAR
        round_with_usd = float(amount_of_usd) / float(avg_price['price'])
        if round_with_usd >= 10:
            dollar_convert = round(round_with_usd)
            print(f"{dollar_convert} is bigger than 10")
        elif round_with_usd >= 1:
            dollar_convert = round(round_with_usd, 2)
            print(f"{dollar_convert} is bigger than 1")
        elif round_with_usd < 0.006:
            str_currency = str(round_with_usd)
            currency = str_currency[:7]
            dollar_convert = float(currency)
            print(f"{dollar_convert} is smaller than 0.0006")
        elif round_with_usd < 0.6:
            print(round_with_usd)
            dollar_convert = round(round_with_usd, 2)
            print(f"{dollar_convert} is smaller than 0.6")
        elif round_with_usd < 1:
            dollar_convert = round(round_with_usd, 4)
            print(f"{dollar_convert} is smaller than 1")
        elif round_with_usd < .005:
            dollar_convert = round(round_with_usd, 5)
            print(f"{dollar_convert} is smaller than 0.005")
        return dollar_convert

    def round_selling_qty_price(self, currency):
        print(type(currency))
        currency = float(currency)
        print(type(currency))
        if currency >= 10:
            dollar_convert = int(currency)
        elif currency >= 1:
            str_currency = str(currency)
            currency = str_currency[:4]
            dollar_convert = float(currency)
        elif currency < 1:
            str_currency = str(currency)
            currency = str_currency[:6]
            dollar_convert = float(currency)
        elif currency < .005:
            dollar_convert = round(currency, 5)
        print(f"{dollar_convert} is final")
        return dollar_convert

    def buy_error_round(self, currency):
        currency_symbol = currency
        avg_price = APICall.client.get_avg_price(symbol=currency_symbol)
        amount_of_usd = Variable.DOLLAR
        round_with_usd = float(amount_of_usd) / float(avg_price['price'])
        dollar_convert = round(round_with_usd)
        return dollar_convert