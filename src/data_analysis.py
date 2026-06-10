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
