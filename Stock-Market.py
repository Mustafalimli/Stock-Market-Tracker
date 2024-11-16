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

# Get Desired Coins Or Stocks Data
def main():
    choice = input("Which data would you like to see? (Stock = 1 / Crypto = 2): ").strip().lower()

    if choice == "1":
        stock_symbol = input("Enter the stock symbol (e.g., AAPL): ").strip().upper()
        price_today, change_percentage = get_stock_data(stock_symbol)
        print(f"{stock_symbol} today's price: {price_today:.2f} USD, Change: {change_percentage:.2f}%")

    elif choice == "2":
        crypto_symbol = input("Enter the cryptocurrency symbol (e.g., BTC/USDT): ").strip().upper()
        price_today, change_percentage = get_crypto_data(crypto_symbol)
        print(f"{crypto_symbol} today's price: {price_today:.2f} USD, Change: {change_percentage:.2f}%")
    
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()
