# Ensemble Backtesting Stock Market

This repository contains the code for an ensemble strategy backtesting on the stock price.
- We ensembled ```Bollinger Bands``` and ```LSTM``` models to predict the stock prices and generate buy/sell/hold signals as 1, -1, 0 respectively.
- We develeoped a module to generate the signals ```generate_signals.py``` and it should be imported from the ```run.ipynb```.
- While running the ```run.ipynb``` the user can specify the stock symbol and the time period for which the backtesting is to be done.But user should ingest his own data with zipline.
- User can also specify the amount of money to be invested and the number of stocks to be bought at each buy signal.
- We bactested our strategy on 50 assets from 10 different sectors and our ensemble strategy outperformed the individual strategies

## Asset Categories
| Industrials | Health Care | Information Technology | Financials | Materials | Consumer Staples | Energy | Communication Services | Utilities | Real Estate |
|-------------|-------------|------------------------|------------|-----------|------------------|--------|-----------------------|-----------|-------------|
| MMM         | ABT         | ADBE                   | AFL        | FMC       | BG               | TRGP   | DIS                   | AES       | ARE         |
| AOS         | BAX         | AMD                    | BAC        | IFF       | MO               | VLO    | WBD                   | LNT       | BXP         |
| BA          | BDX         | AAPL                   | BRK-B         | KLAC      | CPB              | WMB    | GOOGLE                | AEP       | CPT         |
| AXON        | TECH        | CDNS                   | BX         | APD       | STZ              | APA    | FOX                  | AWK       | AMT         |
| CAT         | ALGN        | NVDA                   | COF        | CE        | WMT              | BKR    | EA                    | CEG       | CCI         |

## Project Structure

    ├── Data                <- Folder for all the data used for model training
    │   └── sp50/daily     
    │   
    ├── ML Models           <- Folder for all the machine learning models used for the project
    │       └──LSTM_Stock_Price_Prediction.ipynb
    │
    ├── run.ipynb           <- Jupyter notebook from which the user can run the backtesting
    │
    ├── generate_signal.py  <- Module to generate the buy/sell/hold signals
    │
    └── lstm_12_p50_ckp_13_24_e150.h5   <- LSTM model weights file
--------