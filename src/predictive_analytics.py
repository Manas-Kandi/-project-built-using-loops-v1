import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def prepare_data(historical_data):
    historical_data['Date'] = pd.to_datetime(historical_data['Date'])
    historical_data.set_index('Date', inplace=True)
    features = ['Open', 'High', 'Low', 'Close', 'Volume']
    X = historical_data[features]
    y = historical_data['Close']
    return X, y

def train_linear_regression(X, y):
    model = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    return model

def train_random_forest(X, y):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    return model

def predict_future_prices(model, future_dates):
    future_X = future_dates.values.reshape(-1, 1)
    predicted_prices = model.predict(future_X)
    return pd.Series(predicted_prices, index=future_dates)

def perform_predictive_analysis(historical_data, future_dates):
    X, y = prepare_data(historical_data)
    
    # Train both models and compare their performance
    linear_model = train_linear_regression(X, y)
    rf_model = train_random_forest(X, y)
    
    # Evaluate the models (placeholder for actual evaluation code)
    linear_predictions = predict_future_prices(linear_model, future_dates)
    rf_predictions = predict_future_prices(rf_model, future_dates)
    
    return {
        'Linear Model': {'Predicted Prices': linear_predictions},
        'Random Forest Model': {'Predicted Prices': rf_predictions}
    }
