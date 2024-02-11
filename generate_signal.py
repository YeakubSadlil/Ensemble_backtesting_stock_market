import numpy as np
import pandas as pd
import yfinance as yf
import quantstats as qs
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from os.path import abspath
import sys

ROOT_DIR = abspath("")
sys.path.append(ROOT_DIR)


def calculate_bollinger_bands(prices, dev, window=20):
    """
    Calculate Bollinger Bands for a given series of prices.

    Parameters:
    - prices (pd.Series or np.array): Series of prices.
    - dev (float): Number of standard deviations to use for the bands.
    - window (int, optional): Rolling window size for calculating moving averages. Default is 20.

    Returns:
    - upper_band (float): Upper Bollinger Band.
    - sma (float): Simple Moving Average.
    - lower_band (float): Lower Bollinger Band.
    """

    sma = prices.mean()
    rolling_std = prices.std()
    upper_band = sma + (dev * rolling_std)
    lower_band = sma - (dev * rolling_std)
    return upper_band, sma, lower_band


def plots(results):
    """
    Generate plots comparing strategy returns with a benchmark.

    Parameters:
    - results (pd.DataFrame): DataFrame containing strategy returns.

    Returns:
    - None
    """

    start = results.index[0]
    end = results.index[-1]
    benchmark = yf.download("^GSPC", start=start, end=end)["Adj Close"].pct_change()
    results.index = pd.to_datetime(results.index).tz_convert(None)
    results.index = benchmark.index
    qs.reports.full(
        results["returns"],
        benchmark=benchmark,
        match_dates=True,
        figsize=(8, 4),
        df=results,
    )


# Load the LSTM model outside the function
LSTM_MODEL = load_model("lstm_12_p50_ckp_13_24_e150.h5")
# The model file must in the same folder


def group1_ensemble_model_signals(
    df, lstm_model=LSTM_MODEL, bollinger_bands_window=20, bollinger_bands_dev=1.5
):
    """
    Outputs signal which can take value from the following possible values: [-1, 0, 1]

    Parameters:
    - df (DataFrame): Price DataFrame containing 50 days historical price data.
    - lstm_model (keras.Model, optional): Pre-loaded LSTM model. Defaults to pre-loaded model. The model must in the same folder.
    - bollinger_bands_window (int, optional): Size of the window for Bollinger Bands calculation. Defaults to 20.
    - bollinger_bands_dev (float, optional): Number of standard deviations for Bollinger Bands deviation. Defaults to 1.5.

    Returns:
    - today_signal (int): Signal for the last day based on the provided data and model.
    Possible values: -1 for sell, 0 for hold, 1 for buy.
    """
    prices = df.copy()

    scaler = MinMaxScaler(feature_range=(0, 1))
    prices_scaled = scaler.fit_transform(np.array(prices).reshape(-1, 1))
    prices_scaled_reshaped = prices_scaled.reshape(
        prices_scaled.shape[1], prices_scaled.shape[0], 1
    )

    predicted_price_tomorrow = scaler.inverse_transform(
        lstm_model.predict(prices_scaled_reshaped)
    )[0][0]

    prices_bands = prices.iloc[-(bollinger_bands_window + 1) :]

    upper_band, _, lower_band = calculate_bollinger_bands(
        prices_bands, bollinger_bands_dev, window=bollinger_bands_window
    )

    current_price = prices.iloc[-1]

    signal = 0  # Default signal is hold

    if current_price < lower_band and predicted_price_tomorrow > current_price:
        signal = 1  # Buy Signal
    elif current_price > upper_band and predicted_price_tomorrow < current_price:
        signal = -1  # Sell Signal

    return signal


"""EXAMPLE ZIPLINE CODE:
import generate_signal

def initialize(context):
    context.idx = 0
    context.tickers = sp50tickers
    context.window = 50
    context.buy_stocks = set()
    context.cash_pct = 0.25

# Define the handle_data function
def handle_data(context, data):
    context.idx += 1
    if context.idx < context.window:
        return

    # Execute trades based on the generated signals
    for ticker in context.tickers:
        prices = data.history(symbol(ticker), "price", bar_count=context.window, frequency="1d")
        signal = generate_signal.group1_ensemble_model_signals(prices)
        open_orders = get_open_orders(ticker)

        if ticker not in open_orders:
            if signal == 1 and ticker not in context.buy_stocks:
                if context.portfolio.cash > 0:
                    order_value(symbol(ticker), context.portfolio.cash * context.cash_pct)  # Buy Signal
                    context.buy_stocks.add(ticker)

            elif signal == -1 and ticker in context.buy_stocks:
                order_target_percent(symbol(ticker), 0)  # Sell Signal
                context.buy_stocks.remove(ticker)
        
        

    
# Run the algorithm
results = run_algorithm(
    start=START_DATE,
    end=END_DATE,
    initialize=initialize,
    handle_data=handle_data,
    capital_base=BASE_CAPITAL,
    benchmark_returns=None,
    data_frequency='daily',
    bundle='sp50bundle',
)
generate_signal.plots(results)
"""
