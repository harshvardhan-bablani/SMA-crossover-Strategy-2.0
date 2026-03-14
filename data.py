import yfinance as yf
import pandas as pd


def fetch_data(ticker="AAPL", start="2018-01-01", end="2024-01-01"): #fetching data from 2018 to 2024

    data = yf.download(ticker, start=start, end=end) #downloading 

    data = data[['Close']] #only taking close price

    data.rename(columns={"Close": "price"}, inplace=True) #renaming close to price for easier reference 

    data.dropna(inplace=True) #removing NaN values in current data 

    return data
