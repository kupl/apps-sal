import numpy as np

def max_profit(prices):
    p = np.array(prices)
    return np.array([p[i+1:].max() - prices[i] for i in range(len(prices)-1)]).max()
