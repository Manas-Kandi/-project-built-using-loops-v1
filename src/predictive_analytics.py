import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

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

def train_gradient_boosting(X, y):
    model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    return model

def train_neural_network(X, y):
    model = MLPRegressor(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    return model

def predict_future_prices(model, future_dates):
    future_X = future_dates.values.reshape(-1, 1)
    predicted_prices = model.predict(future_X)
    return pd.Series(predicted_prices, index=future_dates)

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse

def perform_predictive_analysis(historical_data, future_dates):
    X, y = prepare_data(historical_data)
    
    # Train models
    linear_model = train_linear_regression(X, y)
    rf_model = train_random_forest(X, y)
    gb_model = train_gradient_boosting(X, y)
    nn_model = train_neural_network(X, y)
    
    # Evaluate models
    linear_mse = evaluate_model(linear_model, X_test, y_test)
    rf_mse = evaluate_model(rf_model, X_test, y_test)
    gb_mse = evaluate_model(gb_model, X_test, y_test)
    nn_mse = evaluate_model(nn_model, X_test, y_test)
    
    # Select the best model based on MSE
    if linear_mse < rf_mse and linear_mse < gb_mse and linear_mse < nn_mse:
        best_model = linear_model
        best_model_name = 'Linear Model'
    elif rf_mse < linear_mse and rf_mse < gb_mse and rf_mse < nn_mse:
        best_model = rf_model
        best_model_name = 'Random Forest Model'
    elif gb_mse < linear_mse and gb_mse < rf_mse and gb_mse < nn_mse:
        best_model = gb_model
        best_model_name = 'Gradient Boosting Model'
    else:
        best_model = nn_model
        best_model_name = 'Neural Network Model'
    
    # Predict future prices using the best model
    predicted_prices = predict_future_prices(best_model, future_dates)
    
    return {
        best_model_name: {'Predicted Prices': predicted_prices}
    }
