import unittest
import pandas as pd
import numpy as np
import os
from src.data_handling.pre_processing import pre_process

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        # Sample data with missing values and proper DateTime index
        self.sample_data = pd.DataFrame({
            'AAPL': [150.0, 151.0, np.nan, 153.0],
            'MSFT': [210.0, np.nan, 212.0, 213.0],
            'GOOGL': [2700.0, 2720.0, 2730.0, 2740.0]
        }, index=pd.to_datetime(['2023-09-25', '2023-09-26', '2023-09-27', '2023-09-28']))

    def test_pre_process_valid_input(self):
        processed_data = pre_process(self.sample_data)
        # Check if processed_data is a DataFrame
        self.assertIsInstance(processed_data, pd.DataFrame)
        # Check if there are no missing values
        self.assertFalse(processed_data.isnull().values.any())
        # Check if log transformation is applied (log(150) is approx 5.0106)
        self.assertAlmostEqual(processed_data.loc['2023-09-25', 'AAPL'], np.log(150.0), places=4)

    def test_pre_process_non_dataframe_input(self):
        with self.assertRaises(TypeError):
            pre_process([[1, 2], [3, 4]])

    def test_pre_process_empty_dataframe(self):
        empty_df = pd.DataFrame()
        with self.assertRaises(ValueError):
            pre_process(empty_df)

    def test_pre_process_non_positive_values(self):
        # Introduce a non-positive value
        data_with_zero = self.sample_data.copy()
        data_with_zero.loc['2023-09-26', 'AAPL'] = 0
        with self.assertRaises(ValueError):
            pre_process(data_with_zero)

    def tearDown(self):
        # Remove the processed CSV file if it exists
        processed_file = '../data/processed/stock_data_processed.csv'
        if os.path.exists(processed_file):
            os.remove(processed_file)

if __name__ == '__main__':
    unittest.main()
