import requests
import os
import gzip
import shutil

def download_instrument_file_csv(stock_exchange):
    """
    Download and extract the latest CSV file for the given stock exchange.

    Args:
    stock_exchange (str) : The stock exchange for which to download the CSV file.
                           Accepted values are "NSE", "BSE", "MCX", or "complete".
    Raises ValueError: If an invalid stock exchange is provided.
    """
    try:
        url_map = {
            "NSE": "https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz",
            "BSE": "https://assets.upstox.com/market-quote/instruments/exchange/BSE.csv.gz",
            "MCX": "https://assets.upstox.com/market-quote/instruments/exchange/MCX.csv.gz",
            "complete": "https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz"
        }
        if stock_exchange not in url_map:
            raise ValueError("Invalid stock exchange. Accepted values are 'NSE', 'BSE', 'MCX', 'complete'.")
        url = url_map[stock_exchange]
        response = requests.get(url)
        with open(f"{stock_exchange}.csv.gz", 'wb') as f:
            f.write(response.content)
        os.makedirs('csv_files',exist_ok=True)
        with gzip.open(f"{stock_exchange}.csv.gz", 'rb') as f_in:
            with open(f'csv_files/{stock_exchange}.csv', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(f"{stock_exchange}.csv.gz")
    except:
        print(f"new {stock_exchange}.csv file is not available")