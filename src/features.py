"""Feature engineering functions."""
import numpy as np

def log_returns(close_prices):
    """
    Compute log returns: r_t = log(P_t / P_{t-1}).
    """
    return np.log(close_prices[1:] / close_prices[:-1])


def rolling_volatility(returns, window=10):
    """
    Calculate rolling standard deviation. First 'window' elements are NaN.
    """
    vol = []
    for i in range(len(returns)):
        if i < window:
            vol.append(np.nan)
        else:
            vol.append(np.std(returns[i-window:i]))
    return np.array(vol)
