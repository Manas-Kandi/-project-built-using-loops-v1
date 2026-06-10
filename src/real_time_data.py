import requests

API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'
BASE_URL = 'https://www.alphavantage.co/query'

def get_real_time_stock_price(symbol):
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if 'Global Quote' in data:
        return data['Global Quote']['05. price']
    else:
        raise Exception("Failed to retrieve real-time stock price")

if __name__ == "__main__":
    symbol = 'AAPL'
    price = get_real_time_stock_price(symbol)
    print(f"Real-time stock price for {symbol}: ${price}")
