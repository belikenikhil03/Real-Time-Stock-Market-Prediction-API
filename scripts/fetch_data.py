# scripts/fetch_data.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yfinance as yf
import pandas as pd
import time
import schedule
from database.mongo import save_stock_data

def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="5d")

        if data.empty:
            print(f"No data available for ticker {ticker}, please check the ticker or market status.")
            return None

        data = data[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
        data.reset_index(inplace=True)
        data.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)

        print(f"Successfully fetched data for the ticker {ticker}")
        print(data.head())
        return data
    
    except Exception as e:
        print(f"Error fetching data for ticker {ticker}: {e}")
        return None
    
def job():
    tickers = ["TATASTEEL.NS"]
    for ticker in tickers:
        data = fetch_stock_data(ticker)
        if data is not None:
            save_stock_data(ticker, data)
        time.sleep(1)

if __name__ == "__main__":
    # For testing, run the job immediately
    job()
    
    # For scheduled runs (uncomment below)
    # schedule.every(1).hours.do(job)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)