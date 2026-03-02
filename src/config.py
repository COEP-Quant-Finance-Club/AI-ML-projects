"""Project configuration."""

DATA_PATH = "data/ohlcv.csv"

# Feature generation settings
FEATURE_CONFIG = {
    "vol_window": 10,
    "return_lags": 3
}
