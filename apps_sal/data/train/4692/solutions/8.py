import numpy as np


def max_profit(prices):
    p = np.array(prices)
    pr = np.array([])
    for i in range(len(prices) - 1):
        pr = np.append(pr, [p[i + 1:].max() - prices[i]])
    return pr.max()
