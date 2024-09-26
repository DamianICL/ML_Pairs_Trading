import logging
import pandas as pd
import yfinance as yf


# PRE: start_date and end_date exist and in order
def download_stock_data(tickers, start_date, end_date) -> pd.DataFrame:

    try:
        data = yf.download(tickers, start_date, end_date)['Adj Close']

        if data.empty:
            logging.error(f"No data returned for tickers {tickers} from {start_date} to {end_date}")
            raise ValueError("No data available for the specified date range or tickers.")

        return data

    except Exception as e:
        logging.error(f"An error occurred while downloading stock data: {str(e)}")
        raise RuntimeError("Failed to download stock data due to an unexpected error.")

def raw_csv(data):
    data.to_csv('/Users/damino/PycharmProjects/ML_Pairs_Trading/data/raw/stock_data_raw.csv', index = False)


