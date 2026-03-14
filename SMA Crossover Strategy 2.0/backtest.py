import pandas as pd

def run_backtest(data, initial_capital=10000):
    

    df = data.copy()

    cash = initial_capital
    shares = 0

    portfolio_values = []

    for index, row in df.iterrows():

        price = row["price"]
        signal = row["signal"]

        # Buy signal
        if signal == 1:
            shares = cash // price
            cash -= shares * price

        # Sell signal
        elif signal == -1:
            cash += shares * price
            shares = 0

        portfolio_value = cash + shares * price
        portfolio_values.append(portfolio_value)

    df["portfolio_value"] = portfolio_values

    return df