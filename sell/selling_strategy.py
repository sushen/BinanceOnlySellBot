import time

from api_callling.api_calling import APICall


from real_time_data.real_time_data import RealTimeData


from main.all_variable import Variable


from email_option.sending_mail import MailSender
from sell.sell_cripto import SellCripto


class SellingStrategy(RealTimeData):
    def __init__(self, currency, buyingprice):
        self.currency_symbol = currency
        self.buying_price_for_sell = buyingprice

    def selling_condition(self, stop_loss=Variable.STOP_LOSS):
        buying_price = self.buying_price_for_sell
        currency_symbol = self.currency_symbol
        highest_price = []
        while True:
            self.streamKline(currency=currency_symbol.lower(), interval="1m")
            symbol_balance = APICall.client.get_asset_balance(asset=currency_symbol[:-4])
            time.sleep(1)
            symbol_sell_balance = symbol_balance
            currency = float(symbol_sell_balance['free'])
            current_price = float(RealTimeData.append_currency[-1])
            if len(highest_price) == 0:
                highest_price.append(current_price)
            if current_price > highest_price[-1]:
                highest_price.append(current_price)
            highest_price[-1] = float(highest_price[-1])
            current_profit = float(current_price*currency) - float(buying_price*currency)
            print("------------------------------------")
            print(f"|   Trying to Sell {currency}  {self.currency_symbol} Currency  |")
            print("------------------------------------")
            print(f"{current_price}  & total: {current_price*currency} CURRENT PRICE")
            print(f"")
            print(f"{buying_price} & total: {buying_price*currency} BUYING PRICE")
            print(f"{float(highest_price[-1])}  & total: {float(highest_price[-1])*currency} HIGHEST PRICE")
            if buying_price > current_price:
                print(f"{current_profit} CURRENT PROFIT. It's seem you are in loss")
            else:
                print(f"{current_profit} CURRENT PROFIT. It's seem you are in profit")

            increase_buying_price = (float(buying_price) + (
                    float(buying_price) * float(Variable.CHANGE_STOP_LOSS_WHEN_BUYING_PRICE_CHANGE)))
            if current_price > increase_buying_price:
                stop_loss = stop_loss / Variable.STOP_LOSS_QTY
            sell = (highest_price[-1] - (float(highest_price[-1]) * float(stop_loss)))
            print(f"{sell} & Total : {float(sell)*currency}  STOP LOSS SELLING PRICE\n")
            if current_price < (highest_price[-1] - (highest_price[-1] * stop_loss)):
                print(f"{current_profit} : Total profit")
                # Sell.sell_cripto(symbol=currency_symbol)
                SellCripto().sell_cripto(symbol=currency_symbol)
                receiver_mail = Variable.MAIL
                sender = MailSender()

                email_subject = f"We sell {currency_symbol} with Profit : {current_profit} "
                email_body = f"Hi\n We just sell {currency_symbol} currency .\n We make {current_profit} profit. with thanks,\nBinance Bot "

                sender.send_mail(receiver_mail, email_subject, email_body)
                print(f'{email_subject}\n\n {email_body}')

                break


currency = 'FILBUSD'
buyingprice = 9.19

ss = SellingStrategy(currency, buyingprice)
ss.selling_condition()
