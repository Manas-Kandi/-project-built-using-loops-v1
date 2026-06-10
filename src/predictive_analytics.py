import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def prepare_data(historical_data):
    X = historical_data['Date'].values.reshape(-1, 1)
    y = historical_data['Close']
    return X, y

def train_linear_regression(X, y):
    model = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    return model

def predict_future_prices(model, future_dates):
    future_X = future_dates.values.reshape(-1, 1)
    predicted_prices = model.predict(future_X)
    return pd.Series(predicted_prices, index=future_dates)

def perform_predictive_analysis(historical_data, future_dates):
    X, y = prepare_data(historical_data)
    model = train_linear_regression(X, y)
    predicted_prices = predict_future_prices(model, future_dates)
    
    return {
        'Model': model,
        'Predicted Prices': predicted_prices
    }
