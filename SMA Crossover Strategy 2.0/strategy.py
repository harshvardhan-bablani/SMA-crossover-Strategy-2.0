import pandas as pd


def sma_crossover_strategy(data, short_window=20, long_window=50): #defining short and long window

    df = data.copy()

    # Calculate moving averages
    df["SMA_short"] = df["price"].rolling(window=short_window).mean() #short average
    df["SMA_long"] = df["price"].rolling(window=long_window).mean() #long average

    # Remove rows where moving averages are NaN
    df = df.dropna()
    
    ''' 
    creating column position with zero values, setting position as 1 when short average 
    is greater than long average, then for buying or selling signal, we use diff() function to 
    find pivot points, where crossover actually happens. At state of crossover if short average
    is greater then we buy, if short average is smaller then we sell.
    '''

    # Determine market position
    df["position"] = 0
    df.loc[df["SMA_short"] > df["SMA_long"], "position"] = 1 #buying holding signal

    # Detect crossover signals
    df["signal"] = df["position"].diff() #buy and sell signal

    return df   