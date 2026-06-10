import pandas as pd

def calculate_trend(data):
    return data['Close'].diff().mean()

def calculate_moving_average(data, window=50):
    return data['Close'].rolling(window=window).mean()

def calculate_exponential_moving_average(data, span=20):
    return data['Close'].ewm(span=span, adjust=False).mean()

def calculate_relative_strength_index(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_bollinger_bands(data, window=20, std_dev=2):
    rolling_mean = data['Close'].rolling(window=window).mean()
    rolling_std = data['Close'].rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * std_dev)
    lower_band = rolling_mean - (rolling_std * std_dev)
    return {
        'Upper Band': upper_band,
        'Lower Band': lower_band
    }

def analyze_volume(data):
    return {
        'Volume': data['Volume'].sum(),
        'Average Volume': data['Volume'].mean()
    }

# Advanced Technical Indicators
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    short_ema = data['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()
    histogram = macd_line - signal_line
    return {
        'MACD Line': macd_line,
        'Signal Line': signal_line,
        'Histogram': histogram
    }

def calculate_stochastic_oscillator(data, k_period=14, d_period=3):
    low_min = data['Low'].rolling(window=k_period).min()
    high_max = data['High'].rolling(window=k_period).max()
    stoch_k = 100 * (data['Close'] - low_min) / (high_max - low_min)
    stoch_d = stoch_k.rolling(window=d_period).mean()
    return {
        'Stochastic K': stoch_k,
        'Stochastic D': stoch_d
    }

def calculate_atr(data, period=14):
    high_low_diff = data['High'] - data['Low']
    high_prev_close_diff = abs(data['High'] - data['Close'].shift(1))
    low_prev_close_diff = abs(data['Low'] - data['Close'].shift(1))
    true_range = pd.concat([high_low_diff, high_prev_close_diff, low_prev_close_diff], axis=1).max(axis=1)
    atr = true_range.rolling(window=period).mean()
    return atr

# Example usage
if __name__ == "__main__":
    data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=100),
        'Open': [100 + i * 5 for i in range(100)],
        'High': [105 + i * 5 for i in range(100)],
        'Low': [95 + i * 5 for i in range(100)],
        'Close': [100 + i * 5 for i in range(100)],
        'Volume': [1000000 + i * 100000 for i in range(100)]
    })
    
    analysis = {
        'Trend': calculate_trend(data),
        'Moving Average': calculate_moving_average(data),
        'Exponential Moving Average': calculate_exponential_moving_average(data),
        'RSI': calculate_relative_strength_index(data),
        'Bollinger Bands': calculate_bollinger_bands(data),
        'Volume Analysis': analyze_volume(data),
        'MACD': calculate_macd(data),
        'Stochastic Oscillator': calculate_stochastic_oscillator(data),
        'ATR': calculate_atr(data)
    }
    
    for key, value in analysis.items():
        print(f"{key}: {value}")
