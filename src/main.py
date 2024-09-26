from utils.config import STOCK_TICKERS, START_DATE, END_DATE
from data_handling.collection import download_stock_data, raw_csv
from data_handling.pre_processing import pre_process

def main():

    raw_data = download_stock_data(STOCK_TICKERS, START_DATE, END_DATE)
    raw_csv(raw_data)
    pre_process(raw_data)


if __name__ == '__main__':
    main()