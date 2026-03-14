from data import fetch_data
from strategy import sma_crossover_strategy
from backtest import run_backtest
from metrics import calculate_metrics


def main():

    ticker = "AAPL"
    initial_capital = 10000

    # Step 1: fetch data
    data = fetch_data(ticker)

    # Step 2: generate strategy signals
    strategy_data = sma_crossover_strategy(data)

    # Step 3: run backtest
    backtest_data = run_backtest(strategy_data, initial_capital)

    # Step 4: calculate performance metrics
    results = calculate_metrics(backtest_data, initial_capital)

    # Step 5: print results
    print("Strategy Performance")
    print("--------------------")

    for key, value in results.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()