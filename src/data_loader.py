"""Data loading and preprocessing."""
import pandas as pd

def load_ohlcv(csv_path):
    """
    Load OHLCV data from CSV, parse dates, sort, and reset index.

    Args:
        csv_path (str): Path to CSV.
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values('Date', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df
