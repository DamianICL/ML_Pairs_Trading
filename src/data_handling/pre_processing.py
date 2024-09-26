import pandas as pd
import numpy as np
import os

def pre_process(data: pd.DataFrame) -> pd.DataFrame:

    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a Pandas DataFrame")

    if data.empty:
        raise ValueError("Input DataFrame is empty")

    if not isinstance(data.index, pd.DatetimeIndex):
        raise TypeError("DataFrame index must be a Pandas DatetimeIndex")

    full_dates = pd.date_range(start=data.index.min(), end=data.index.max(), freq='B')  # 'B' for business days
    data = data.reindex(full_dates)
    data_ffill = data.ffill()
    data_filled = data_ffill.bfill()

    if data_filled.isnull().values.any(): # Checks no missing values
        raise ValueError("Missing values remain after forward-fill and backward-fill")

    if (data_filled <= 0).any().any(): # Checks no non-positive values
        raise ValueError("Data contains non-positive values, cannot apply log transformation")

    data_log = np.log(data_filled)

    processed_dir = os.path.join(os.path.dirname(__file__), '../../data/processed/')
    os.makedirs(processed_dir, exist_ok=True)
    processed_file_path = os.path.join(processed_dir, 'stock_data_processed.csv')

    try:
        data_log.to_csv(processed_file_path, index=True)
    except Exception as e:
        raise IOError(f"Failed to save processed data: {e}")

    return data_log


