import requests
import datetime as dt
from secrets import STOCK_API_KEY, NEWS_API_KEY

# CONSTANTS
STOCK = 'TSLA'
COMPANY_NAME = 'Tesla Inc'

# DATETIME SETTINGS
today = dt.datetime.now().date()
yesterday = dt.datetime.now().date() - dt.timedelta(days=1)
day_before = dt.datetime.now().date() - dt.timedelta(days=2)

# STOCK API SETTINGS
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}
stock_response = requests.get('https://www.alphavantage.co/query', params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

# NEWS API SETTINGS
news_params = {
    'q': 'Tesla',
    'from':  yesterday,
    'sortyBy': 'popularity',
    'apiKey': NEWS_API_KEY,
    'source': 'us',
}
news_response = requests.get('https://newsapi.org/v2/top-headlines?', params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
print(news_data)

# GET YESTERDAY AND DAY BEFORE CLOSE AND OPENING PRICES
yesterday_stock = stock_data['Time Series (Daily)'][f'{yesterday}']['1. open']
day_before_stock = stock_data['Time Series (Daily)'][f'{day_before}']['4. close']

# PERCENTAGE DIFFERENCE BETWEEN 2 DAYS
difference = (float(yesterday_stock) * 100) / float(day_before_stock)

if difference < 96:
    print('Get News')

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
