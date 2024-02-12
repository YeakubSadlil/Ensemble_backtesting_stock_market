<h1 align="center">
  📈 Ensemble Strategy for Backtesting Stock Market 📊
</h1>
<p align="center"> 
<strong>This repository contains An Ensemble Strategy for Backtesting Stock Price, Combining Bollinger Bands and LSTM Models.</strong>
</p>

## 📚 Table of Contents

- [📖 User Manual](#📖-user-manual)
  - [🔧 Setup](#setup)
  - [🔨 Install Dependencies](#install-dependencies)
  - [📥 Data Ingestion](#data-ingestion)
  - [🏃‍♂️ Running the Notebook](#running-the-notebook)
  - [📊 Interpreting Results](#interpreting-results)
- [🏗️ Project Structure](#🏗️-project-structure)
- [🛠️ Our Approach](#🛠️-our-approach)
- [🔮 Future Works](#🔮-future-works)
- [📊 Asset Categories](#📂-asset-categories)

## 📖 User Manual

1. **🔧 Setup**: Clone or download, get a copy of this repository<br>
```git clone https://github.com/YeakubSadlil/Ensemble_backtesting_stock_market.git```
2. **🔨 Install Dependencies**: Install the required dependencies using the following command<br>
```pip install -r requirements.txt```
3. **📥 Data Ingestion**: Ingest your own data with zipline (the strategy can accept multi assets).
4. **🏃‍♂️ Running the Notebook**: Open the repo and run `run.ipynb` and customize your backtesting parameters stock symbols, time period, investment settings like amount and number of stocks to buy at each buy signal etc.
5. **📊 Interpreting Results**: A ```quantstats``` report will be generated at the end by ```gs.plots(results)``` .Analyze the generated plots and results to assess the strategy's performance.

## 🏗️ Project Structure

    ├── 📂 Data                <- Folder for all the data used for model training
    │   └── sp50/daily     
    │   
    ├── 📂 ML Models           <- Folder for all the machine learning models used for the project
    │       └──LSTM_Stock_Price_Prediction.ipynb
    │
    ├── 📓 run.ipynb           <- Jupyter notebook from which the user can run the backtesting
    │
    ├── 📄 generate_signal.py  <- Module to generate the buy/sell/hold signals
    │
    ├── 📝 requirements.txt    <- List of of required python packages
    │
    └── 📄 lstm_12_p50_ckp_13_24_e150.h5   <- LSTM model weights file
--------

## 🛠️ Our Approach

- **Ensemble Strategy**: We combined Bollinger Bands and LSTM models to predict stock prices and generate signals.
    - When LSTM model predicts the tomorrow's stock price is higher than the current price and Bollinger Bands lower band is also higher than the current price, then we generate a buy signal (Long Position)
    - When LSTM model predicts the tomorrow's stock price is lower than the current price and Bollinger Bands upper band is also lower than the current price, then we generate a sell signal.
    - Otherwise, we generate a hold signal.
- **Bollinger Bands**: Utilized the Bollinger Bands model to generate buy/sell signals based on the stock's price volatility with a default window of 20 days.
- **LSTM Model**: Developed an LSTM model to predict stock price of the next day based on the previous 50 days of stock prices. 
    - Used it as a filter with Bollinger Bands to generate signals.
    - Trained the model on S&P 500 data from 2013 to 2020 and tested it on data from 2023 to 2024. 📅
- **Asset Categorization**: Backtested our strategy on 50 assets from 10 different sectors (2018-2022) to add diversification and evaluate its performance. Check [Asset Lists](#📂-asset-categories) or the  [Data](https://github.com/YeakubSadlil/Ensemble_backtesting_stock_market/blob/01acf517e821f63eaabbcf972c3fbc51a196a4b3/Data/sp50) section to see the list of assets.  
- **Module Development**: Developed a module to generate signals (`generate_signals.py`), which is imported into the `run.ipynb`. It will return buy/sell/hold signals as 1, -1, 0 respectively.
- **Backtesting**: Utilized the `zipline` library to backtest our strategy and evaluate the performance. 🧪

## 🔮 Future Works
- **Dataset Choosing**: We have trained the model on S&P 500 data, but can created an market index with the 50 assets we have used for backtesting.
- **Order Strategy**: As the market is a bull market we went only long positions but with proper short selling strategy more profit can be generated.
- **Fine-Tuning Models**: Continuously refine and optimize the Bollinger Bands window size and LSTM models for better prediction accuracy. 🔧
- **Risk Management**: Implement risk management strategies to minimize potential losses like as stop loos and take profit.

## 📂 Asset Categories
| Industrials | Health Care | Information Technology | Financials | Materials | Consumer Staples | Energy | Communication Services | Utilities | Real Estate |
|-------------|-------------|------------------------|------------|-----------|------------------|--------|-----------------------|-----------|-------------|
| MMM         | ABT         | ADBE                   | AFL        | FMC       | BG               | TRGP   | DIS                   | AES       | ARE         |
| AOS         | BAX         | AMD                    | BAC        | IFF       | MO               | VLO    | WBD                   | LNT       | BXP         |
| BA          | BDX         | AAPL                   | BRK-B         | KLAC      | CPB              | WMB    | GOOGLE                | AEP       | CPT         |
| AXON        | TECH        | CDNS                   | BX         | APD       | STZ              | APA    | FOX                  | AWK       | AMT         |
| CAT         | ALGN        | NVDA                   | COF        | CE        | WMT              | BKR    | EA                    | CEG       | CCI         |

