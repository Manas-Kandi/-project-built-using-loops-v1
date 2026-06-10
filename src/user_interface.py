import argparse
from .data_integration import integrate_real_time_data, integrate_historical_data, integrate_predictive_data

def main():
    parser = argparse.ArgumentParser(description="Stock Market Analyzer")
    subparsers = parser.add_subparsers(dest='command')

    # Real-time data integration command
    real_time_parser = subparsers.add_parser('real-time', help='Integrate real-time stock price data')
    real_time_parser.set_defaults(func=integrate_real_time_data)

    # Historical data analysis command
    historical_parser = subparsers.add_parser('historical', help='Analyze historical stock prices')
    historical_parser.add_argument('--symbol', type=str, required=True, help='Stock symbol to analyze')
    historical_parser.add_argument('--start_date', type=str, required=True, help='Start date in YYYY-MM-DD format')
    historical_parser.add_argument('--end_date', type=str, required=True, help='End date in YYYY-MM-DD format')
    historical_parser.set_defaults(func=integrate_historical_data)

    # Predictive analytics command
    predictive_parser = subparsers.add_parser('predictive', help='Predict future stock prices')
    predictive_parser.add_argument('--symbol', type=str, required=True, help='Stock symbol to predict')
    predictive_parser.add_argument('--start_date', type=str, required=True, help='Start date in YYYY-MM-DD format')
    predictive_parser.add_argument('--end_date', type=str, required=True, help='End date in YYYY-MM-DD format')
    predictive_parser.set_defaults(func=integrate_predictive_data)

    args = parser.parse_args()
    result = args.func(**vars(args))
    print(result)

if __name__ == "__main__":
    main()
