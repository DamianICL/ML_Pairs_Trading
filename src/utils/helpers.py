import numpy as np
import pandas as pd
from utils.config import STOCK_TICKERS

def log_transform(data):
    data[:] = np.log(data)

def to_long_data(wide_data: pd) -> pd.DataFrame:
    melted_data = wide_data.melt(id_vars='Date',value_vars = STOCK_TICKERS, var_name='Stock', value_name='Price')
    sorted_melted_data = melted_data.sort_values(by='Date', ascending=True) # sort as a good practice check
    return sorted_melted_data

def to_date_time(data: pd.DataFrame) -> pd.DataFrame:
    if not pd.api.types.is_datetime64_any_dtype(data['Date']):
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    return data
