from .real_time_data import get_real_time_stock_price

def integrate_real_time_data():
    symbols = ['AAPL', 'GOOGL', 'MSFT']
    prices = {symbol: get_real_time_stock_price(symbol) for symbol in symbols}
    return prices

if __name__ == "__main__":
    real_time_prices = integrate_real_time_data()
    print(real_time_prices)
