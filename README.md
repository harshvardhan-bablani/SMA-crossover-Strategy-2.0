# SMA Crossover Strategy Backtester

This project implements a simple algorithmic trading strategy based on a **Simple Moving Average (SMA) crossover**. The system downloads historical stock price data, generates trading signals, simulates trades using a backtesting engine, and evaluates the strategy's performance.

The strategy is tested on historical price data for **AAPL (Apple Inc.)** using Python.

---

## Strategy Overview

The trading strategy uses two moving averages:

- **Short-term SMA (20 days)**
- **Long-term SMA (50 days)**

Trading rules:

- **Buy Signal:** When the short SMA crosses above the long SMA
- **Sell Signal:** When the short SMA crosses below the long SMA

The backtester simulates trades using an initial capital of **$10,000**.

---

## Project Structure
```
SMA-crossover-strategy-2.0/
│
├── data.py      -Downloads and prepares historical price data
├── strategy.py  -Implements the SMA crossover strategy
├── backtest.py  -Simulates trades and portfolio performance
├── metrics.py   -Calculates strategy performance metrics
├── main.py      -Runs the complete trading pipeline
└── README.md

```
---

## Features

- Fetch historical stock data using Yahoo Finance
- Compute technical indicators (SMA)
- Generate buy and sell signals
- Simulate trading with a simple backtesting engine
- Evaluate strategy performance with key metrics

---

## Performance Metrics

The system calculates:

- Final portfolio value
- Total strategy return
- Buy-and-hold return
- Number of trades executed

These metrics allow comparison between the strategy and a passive investment approach.

---

## Technologies Used

- Python
- pandas
- NumPy
- yfinance

---

## How to Run

1. Install required packages
```
pip install pandas numpy yfinance
```
3. Run the program
```
python main.py
```


The program will:

1. Download historical stock data
2. Generate trading signals
3. Simulate trades
4. Calculate strategy performance

---

## Example Output
```
Strategy Performance
Final Portfolio Value: 11850
Total Strategy Return: 0.185
Buy and Hold Return: 0.23
Number of Trades: 14
```


---

## Future Improvements

Possible extensions for the project include:

- Visualization of equity curves
- Sharpe ratio and additional risk metrics
- Parameter optimization for moving averages
- Testing across multiple assets
