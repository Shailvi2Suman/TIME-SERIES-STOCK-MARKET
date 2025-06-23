# TIME-SERIES-STOCK-MARKET

# 📈 Stock Market Forecasting using ARIMA, SARIMA & LSTM

This project aims to analyze and forecast stock prices using both classical statistical methods (ARIMA, SARIMA) and deep learning (LSTM). It includes detailed EDA, engineered features, and interactive dashboards built using Streamlit and Power BI.

---

## 📌 Problem Statement

Can we forecast stock price movements using historical data and time series modeling?
This project attempts to answer that by:

* Exploring the stock price trends, volatility, and patterns over time
* Applying ARIMA and SARIMA for traditional forecasting
* Using LSTM (a deep learning model) to capture sequential patterns
* Visualizing results with both code-based and no-code dashboards

---

## 🔍 Exploratory Data Analysis (EDA)

* Line plots for Open, High, Low, Close, Volume
* Moving Averages (MA20, MA50)
* Daily Returns and Volatility
* Correlation analysis
* Seasonality & trend decomposition (additive)

All visualizations are available in eda\_dashboard.html and Streamlit.

---

## 📈 Forecasting Models

### 1. ARIMA

Autoregressive Integrated Moving Average — used as a baseline model for univariate time series.

### 2. SARIMA

Seasonal ARIMA to incorporate both trend and seasonal components in the series.

### 3. LSTM (Long Short-Term Memory)

A type of Recurrent Neural Network used for sequence prediction. Captures complex, non-linear dependencies in stock movements.

Each model’s predictions were compared against actuals using test data and RMSE.

---

## 💻 Dashboards

✅ Streamlit
Launch app.py using:

```bash
streamlit run app.py
```

Includes navigation tabs for:

* EDA (Python)
* Forecasting models
* HTML dashboards

✅ Power BI
Also includes a no-code dashboard for interactive, professional reporting using slicers and analytics.

---

## ⚙️ Technologies Used

| Domain        | Tools / Libraries                              |
| ------------- | ---------------------------------------------- |
| Programming   | Python 3.10 (recommended)                      |
| Data Analysis | pandas, numpy                                  |
| Visualization | matplotlib, seaborn, plotly                    |
| Forecasting   | statsmodels (ARIMA, SARIMA), tensorflow (LSTM) |
| Dashboards    | Streamlit, Power BI                            |
| Environment   | Jupyter Notebook, VS Code, GitHub              |

---

## 🚀 How to Run

1. Clone this repository

```bash
git clone https://github.com/Shailvi2Suman/TIME-SERIES-STOCK-MARKET.git
cd TIME-SERIES-STOCK-MARKET
```

2. (Optional) Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate    # On Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the Streamlit dashboard

```bash
streamlit run app.py
```

5. Open eda\_dashboard.html manually or from the dashboard dropdown.

---

## ✨ Results Snapshot

* LSTM captured long-term dependencies and showed better performance for volatile periods.
* SARIMA improved upon ARIMA by modeling seasonality and trend.
* All models were visualized for side-by-side comparison.

---

## 📌 Future Improvements

* Include more stock symbols or multiple stocks
* Add technical indicators (MACD, RSI)
* Real-time data fetching using yfinance or APIs
* Hyperparameter tuning for LSTM and SARIMA
* Deploy Streamlit on a cloud platform with user input features


