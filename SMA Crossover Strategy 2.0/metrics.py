def calculate_metrics(data, initial_capital=10000):
    """
    Calculate basic performance metrics for the trading strategy.
    """

    final_portfolio_value = data["portfolio_value"].iloc[-1]

    total_return = ((final_portfolio_value - initial_capital) / initial_capital)*100

    buy_hold_return = 100* ((
        data["price"].iloc[-1] - data["price"].iloc[0]
    ) / data["price"].iloc[0])

    num_trades = data["signal"].abs().sum()

    metrics = {
        "Final Portfolio Value": final_portfolio_value,
        "Total Strategy Return": total_return,
        "Buy and Hold Return": buy_hold_return,
        "Number of Trades": num_trades
    }

    return metrics