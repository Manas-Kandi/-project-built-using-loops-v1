import pandas as pd

def calculate_trend(data):
    return data['Close'].diff().mean()

def calculate_moving_average(data, window=50):
    return data['Close'].rolling(window=window).mean()

def analyze_volume(data):
    return {
        'Volume': data['Volume'].sum(),
        'Average Volume': data['Volume'].mean()
    }

def perform_historical_analysis(historical_data):
    trend = calculate_trend(historical_data)
    moving_average = calculate_moving_average(historical_data)
    volume_analysis = analyze_volume(historical_data)
    
    return {
        'Trend': trend,
        'Moving Average': moving_average,
        'Volume Analysis': volume_analysis
    }
