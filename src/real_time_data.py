import requests

API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'
BASE_URL = 'https://www.alphavantage.co/query'

def get_real_time_stock_price(symbols):
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': ','.join(symbols),
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    prices = {}
    if 'Global Quote' in data:
        for symbol, quote in data['Global Quote'].items():
            if '05. price' in quote:
                prices[symbol.split('.')[1]] = quote['05. price']
    else:
        raise Exception("Failed to retrieve real-time stock prices")
    
    return prices

if __name__ == "__main__":
    symbols = ['AAPL', 'GOOGL', 'MSFT']
    prices = get_real_time_stock_price(symbols)
    print(prices)
