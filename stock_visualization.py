import requests
import pygal
from lxml import etree
from datetime import datetime
import webbrowser

def get_stock_data(symbol, function):
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval=5min&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

def process_data(data, start_date, end_date):
    time_series = data.get("Time Series (Daily)", {})
    dates = []
    open_prices = []
    high_prices = []
    low_prices = []
    closing_prices = []
    
    for date, values in time_series.items():
        if start_date <= date <= end_date:
            dates.append(date)
            open_prices.append(float(values['1. open']))  # Use '1. open' for open price
            high_prices.append(float(values['2. high']))   # Use '2. high' for high price
            low_prices.append(float(values['3. low']))     # Use '3. low' for low price
            closing_prices.append(float(values['4. close']))  # Use '4. close' for closing price

    return dates, open_prices, high_prices, low_prices, closing_prices