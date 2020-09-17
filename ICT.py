#yudin
import requests
import json
from datetime import *; from dateutil.relativedelta import *
import calendar

# url = https://api.tiingo.com/tiingo/daily/MSFT/prices + ?date=2020-05-20&token=f8e0228db0b5122cf7f09c0f4a74a8f017a8db5c

TODAY = date.today()
nowaday = TODAY - relativedelta(days=1)

def get_stock_data(ticker, period):
    historical_date = get_historical_date_by_period(period)
    historical_price = get_stock_price_by_date(ticker, historical_date)
    current_price = get_stock_price_by_date(ticker, nowaday)
    price_change = get_price_change(historical_price, current_price)
    formatted_price_change = get_formatted_price_change_string(price_change)
    return round(historical_price, 2), round(current_price, 2), formatted_price_change


def get_historical_date_by_period(period): #period is yy-m-d
    period = period.split('-')
    y = int(period[0])
    mo = int(period[1])
    d = int(period[2])
    historical_date = TODAY - relativedelta(years=y, months=mo, days=d)
    return historical_date


def get_stock_price_by_date(ticker, mydate):
    url = 'https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate={mydate}&token=f8e0228db0b5122cf7f09c0f4a74a8f017a8db5c'.format(ticker=ticker, mydate=mydate)
    # getting url with variable date and ticker
    tickerdata = requests.get(url)
    close_cost = tickerdata.json()[0]['adjClose']  # close cost of the stock
    return close_cost


def get_price_change(historical_price: float, current_price: float):
    price_change = current_price/historical_price
    return price_change


def get_formatted_price_change_string(price_change):
    formatted_price_change = price_change*100
    return round(formatted_price_change, 2)


print(get_stock_data('AAPL', '0-3-2'))