from .real_time_data import get_real_time_stock_price
from .data_analysis import perform_historical_analysis

def integrate_real_time_data():
    symbols = ['AAPL', 'GOOGL', 'MSFT']
    prices = {symbol: get_real_time_stock_price(symbol) for symbol in symbols}
    return prices

def integrate_historical_data(symbols, start_date, end_date):
    historical_prices = {}
    for symbol in symbols:
        # Placeholder for fetching historical data
        historical_prices[symbol] = pd.DataFrame({
            'Date': pd.date_range(start=start_date, end=end_date),
            'Close': [100 + i * 5 for i in range((end_date - start_date).days)]
        })
    
    return {symbol: perform_historical_analysis(price_data) for symbol, price_data in historical_prices.items()}

if __name__ == "__main__":
    real_time_prices = integrate_real_time_data()
    print(real_time_prices)
