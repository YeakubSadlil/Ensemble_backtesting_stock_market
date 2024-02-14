<!-- <div align="right">
  <img align="center" src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Blue_Python_3.8_Shield_Badge.svg" alt="python 3.8" height="20" width="60" />
</div> -->


![Static Badge](https://img.shields.io/badge/python-3.10-a?style=plastic&logo=python)
![Static Badge](https://img.shields.io/badge/zipline--reloaded-3.0.3-a?style=plastic&labelColor=red)
![Static Badge](https://img.shields.io/badge/os-ubuntu-a?style=plastic&logo=ubuntu&labelColor=blue)
![Static Badge](https://img.shields.io/badge/quantstats-0.0.62-a?style=plastic&labelColor=blue&color=purple)
![Static Badge](https://img.shields.io/badge/keras-2.15.0-a?style=plastic&labelColor=blue)
![Static Badge](https://img.shields.io/badge/jupyter--notebook-7-a?style=plastic&logo=jupyter&labelColor=blue)





<h1 align="center">
  📈 Ensemble Strategy for Backtesting Stock Price
</h1>
<p align="center"> 
<strong>This repository contains An Ensemble Strategy for Backtesting Stock Price, Combining Bollinger Bands and LSTM Models.</strong>
</p>

<!-- <div align="right">
  <details>
    <summary><b>Technical Environment</b></summary>
    <div align="right">
      <img align="center" src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Blue_Python_3.8_Shield_Badge.svg" alt="python 3.8" height="25" width="70" />
    </div>
    <div align="right">
      <img align="center" src="https://miro.medium.com/v2/resize:fit:1400/format:webp/0*7mcenkTaprqVx17y.jpg" alt="python 3.8" height="25" width="70" style="vertical-align: -18px;/>
    </div>

    
  </details>
</div> -->

##  📚 Table of Contents

- [ 📖 User Manual](#-user-manual)
  - [ Setup](#setup)
  - [ Install Dependencies](#install-dependencies)
  - [ Data Ingestion](#data-ingestion)
  - [ Running the Notebook](#️running-the-notebook)
  - [ Interpreting Results](#interpreting-results)
- [️ 🏗️ Project Structure](#️-project-structure)
- [️ 🛠️ Our Approach](#️-our-approach)
- [ 🔮 Future Works](#-future-works)
- [ 📂 Asset Categories](#-asset-categories)

<!-- ## 📖 User Manual
### 1. Manual Installation
1. **🔧 Setup**: Clone or download, get a copy of this repository<br>
```git clone https://github.com/YeakubSadlil/Ensemble_backtesting_stock_market.git```
2. **🔨 Install Dependencies**: Install the required dependencies using the following command<br>
make sure that you have `python 3.10` installed or create a new environment.<br>
```pip install -r requirements.txt```
3. **📥 Data Ingestion**: Ingest your own data with zipline (the strategy can accept multi assets).
4. **🏃‍♂️ Running the Notebook**: Open the repo and run `run.ipynb` and customize your backtesting parameters stock symbols, time period, investment settings like amount and number of stocks to buy at each buy signal etc.
5. **📊 Interpreting Results**: A ```quantstats``` report will be generated automatically at the end by ```gs.plots(results)``` .<br>
Analyze the generated plots and results to assess the strategy's performance on the selected assets.

### 2. Docker Installation
1. **Prerequisites:** Verify you have `Docker` installed and running.
1. **🔧 Setup**: Clone or download, get a copy of this repository
2. **Build the Docker Image**: ```docker build -t ensemble-backtest-stockprice .```
3. **Run the Docker Container**: ```docker run -d -p 8888:8888 --name my_backtest_container ensemble-backtest-stockprice```
4. **Get the Jupyter Notebook Token**: ```docker exec -it my_backtest_container /bin/bash```<br>
```jupyter server list ```
5. **Access Jupyter Notebook**: Open your web browser and go to ```http://localhost:8888.``` Paste the copied token when prompted(If no token is required then skip the step)

From the jupyter notebook run `run.ipynb`. -->

## 📖 User Manual

### 1. Manual Installation

Follow these steps for a manual installation:

1. **Clone the Repository**: Get a copy of this repository on your local machine with the following command:<br>
```git clone https://github.com/YeakubSadlil/Ensemble_backtesting_stock_market.git```

2. **Install Dependencies**: Make sure you have `Python 3.10` installed. Then, install the required dependencies using the following command:<br>
```pip install -r requirements.txt```

3. **Data Ingestion**: Ingest your own data with Zipline.Threre is a default data ingestion available on the notebook. Note that the strategy can accept multiple assets.

4. **Run the Notebook**: Open the `run.ipynb` file in the repository and customize your backtesting parameters such as stock symbols, time period, and investment settings like amount and number of stocks to buy at each buy signal.

5. **Interpret Results**: A `quantstats` report will be generated automatically at the end by `gs.plots(results)`.<br>
Analyze the generated plots and results to assess the strategy's performance on the selected assets.

N.B. If you don't want to customize any input parameters or data ingestion, you can directly run the notebook `run.ipynb` without any changes.

### 2. Docker Installation

If you have Docker installed, you can use it to run the project to avoid setting the environment or installing dependencies:

1. **Verify Docker Installation**: Make sure Docker is installed and running on your machine.

2. **Clone the Repository**: Get a copy of this repository on your local machine with the following command:<br>
```git clone https://github.com/YeakubSadlil/Ensemble_backtesting_stock_market.git```

3. **Build the Docker Image**: Run the following command to build the Docker image:<br>
```docker build -t ensemble-backtest-stockprice .```

4. **Run the Docker Container**: Start a new Docker container with the image using the following command:<br>
```docker run -d -p 8888:8888 --name my_backtest_container ensemble-backtest-stockprice```

5. **Access Jupyter Notebook**: Open your web browser and go to `http://localhost:8888`. Paste the copied token when prompted. (If no token is required, you can skip step 6).

6. **Get the Jupyter Notebook Token**: Run the following commands to get the Jupyter Notebook token:<br>
```docker exec -it my_backtest_container /bin/bash```<br>
After that, run the following command inside from the container that you run:<br>
```jupyter server list ```<br>
It will show you a link with a token. Copy the token and paste it in the browser jupyter notebook prompt.


From the Jupyter Notebook, run `run.ipynb` to start the project.


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
    ├── 🐳 Dockerfile          <- Dockerfile for building the Docker image
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
- **Asset Categorization**: Backtested our strategy on 50 assets from 10 different sectors (2018-2022) to add diversification and evaluate its performance. Check [Asset Lists](#-asset-categories) or the  [Data](https://github.com/YeakubSadlil/Ensemble_backtesting_stock_market/blob/01acf517e821f63eaabbcf972c3fbc51a196a4b3/Data/sp50) section to see the list of assets.  
- **Module Development**: Developed a module to generate signals (`generate_signals.py`), which is imported into the `run.ipynb`. It will return buy/sell/hold signals as 1, -1, 0 respectively.
- **Backtesting**: Utilized the `zipline` library to backtest our strategy and `quantstats` to evaluate the performance. 🧪
- **Performance Analysis**: Our ensemble strategy is pretty close to the Bollinger Bands individual strategy, but it has outperformed the benchmark (S&P 500) in terms of CAGR, Sharpe Ratio, Portfolio Value while bactested with 50 assets from 2018-22.<br>
It coudn't beat the benchmark while backtested with some single assets for out sample data but performed well for the ```AAPL``` stock.

## 🔮 Future Works
- **Dataset Choosing**: We have trained the LSTM model on S&P 500 data, but can be created an market index with the 50 assets that we have used for backtesting.
- **Order Strategy**: As the market is a bull market we went only long positions but with proper short selling strategy more profit can be generated.
- **Fine-Tuning Models**: Continuously refine and optimize the Bollinger Bands window size and LSTM models for better prediction accuracy. The LSTM model underperforming while predicting based on past 100 and 150 days.LSTM may suffer from vanishing gradients and can be improved with `Attention mechanisms`, `Stacking more layers` or ```Bidirectional LSTMs``` etc.🔧
- **Risk Management**: Implement risk management strategies to minimize potential losses like as stop loos and take profit.
- **Meta-Labeling Strategy**: In his book Advances in Financial Machine Learning, Dr.Lopez de Prad describes a Meta-labeling technique that uses an array of new Ensemble learning techniques to enhance machine learning strategies. Hudson & Thames a research group expands on these techniques and showed some implementation ideas in [youtube video.](https://youtu.be/1fYzABjsNFk?si=G6HPDBBNlsNotGk5)
## 📂 Asset Categories
| Industrials | Health Care | Information Technology | Financials | Materials | Consumer Staples | Energy | Communication Services | Utilities | Real Estate |
|-------------|-------------|------------------------|------------|-----------|------------------|--------|-----------------------|-----------|-------------|
| MMM         | ABT         | ADBE                   | AFL        | FMC       | BG               | TRGP   | DIS                   | AES       | ARE         |
| AOS         | BAX         | AMD                    | BAC        | IFF       | MO               | VLO    | WBD                   | LNT       | BXP         |
| BA          | BDX         | AAPL                   | BRK-B         | KLAC      | CPB              | WMB    | GOOGLE                | AEP       | CPT         |
| AXON        | TECH        | CDNS                   | BX         | APD       | STZ              | APA    | FOX                  | AWK       | AMT         |
| CAT         | ALGN        | NVDA                   | COF        | CE        | WMT              | BKR    | EA                    | CEG       | CCI         |

