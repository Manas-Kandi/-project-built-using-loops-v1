import requests

API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'
BASE_URL = 'https://www.alphavantage.co/query'

def get_real_time_stock_price(symbols):
    prices = {}
    for symbol in symbols:
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if 'Global Quote' in data:
            price = data['Global Quote']['05. price']
            prices[symbol] = price
        else:
            raise Exception(f"Failed to retrieve real-time stock price for {symbol}")
    
    return prices

if __name__ == "__main__":
    symbols = ['AAPL', 'GOOGL', 'MSFT']
    prices = get_real_time_stock_price(symbols)
    print(prices)
