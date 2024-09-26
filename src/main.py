from utils.config import STOCK_TICKERS, START_DATE, END_DATE
from data_handling.collection import download_stock_data, raw_csv

def main():
    raw_data = download_stock_data(STOCK_TICKERS, START_DATE, END_DATE)
    raw_csv(raw_data)


if __name__ == '__main__':
    main()