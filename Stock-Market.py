import yfinance as yf
import requests
import ccxt

def get_stock_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    hist = stock.history(period="2d")  # Last 2 Days data
    today_data = hist.iloc[-1]
    yesterday_data = hist.iloc[-2]

    price_today = today_data['Close']
    price_yesterday = yesterday_data['Close']
    
    change_percentage = ((price_today - price_yesterday) / price_yesterday) * 100
    return price_today, change_percentage
# API 
def get_crypto_data(crypto_symbol):
    exchange = ccxt.binance()  # Binance
    ticker = exchange.fetch_ticker(crypto_symbol)
    
    price_today = ticker['close']
    price_yesterday = ticker['open']  # Yesterday's open price
    change_percentage = ((price_today - price_yesterday) / price_yesterday) * 100
    return price_today, change_percentage
