"""Evaluation metrics."""
import numpy as np

def sharpe_ratio(returns, risk_free_rate=0.0):
    """
    Calculate Sharpe Ratio: Mean(Excess Returns) / Std(Excess Returns).
    """
    excess = returns - risk_free_rate
    if np.std(excess) == 0:
        return 0.0
    return np.mean(excess) / np.std(excess)


def max_drawdown(pnl_curve):
    """
    Calculate Maximum Drawdown (MDD) from peak to trough.
    """
    peak = pnl_curve[0]
    max_dd = 0
    for value in pnl_curve:
        peak = max(peak, value)
        dd = (peak - value) / peak
        max_dd = max(max_dd, dd)
    return max_dd
