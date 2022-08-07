from pprint import pprint

# from api_callling.api_calling import APICall
#
# from error_handleing.round import PriceRound

import os

import binance

# from error_handleing.exception_handleing import BinanceAPIException

api_key = os.environ.get('binance_api_key')
api_secret = os.environ.get('binance_api_secret')
from binance.client import Client
client = Client(api_key, api_secret)


class SellCripto:
    """
    You need currency as quantity and symbol as symbol
    """

    def round_qty_price(self, currency):
        if float(currency) >= 10:
            dollar_convert = int(currency)
            print(f"{dollar_convert} is bigger than 10")

        elif float(currency) >= 1:
            dollar_convert = float(currency)
            print(f"{dollar_convert} is bigger than 1")

        elif 1 > float(currency) > .005:
            dollar_convert = str(currency)
            dollar_convert = float(dollar_convert)
            print(f"{dollar_convert} is smaller than 1 and bigger than .005")
        elif float(currency) < .005:
            dollar_convert = str(currency)[0:-1]
            dollar_convert = float(dollar_convert)

        print(f"Rounded Figur :{dollar_convert}")
        return dollar_convert

    def sell_cripto(self, symbol):
        fees = client.get_trade_fee(symbol=symbol)
        print(fees)
        symbol_fees = fees[0]['takerCommission']
        symbol_fees = float(symbol_fees) * 1000
        print(symbol_fees)
        quantity = 100 - symbol_fees
        print(int(quantity))
        # fees = fees[0]['symbol']
        balance = client.get_asset_balance(asset=symbol[:-4])
        print(balance)
        symbol_balance = float(balance['free'])
        print(symbol_balance)
        # print(input("Stop:"))

        # qty = PriceRound.round_selling_qty_price(self, currency)
        order = client.order_market_sell(
            symbol=symbol,
            quantity=self.round_qty_price(symbol_balance)
        )

        pprint(order)


# SellCripto().sell_cripto("BICOBUSD")
# try:
#     pass
# except binance.exceptions.BinanceAPIException as e:
#     print(e)
