from itertools import islice

def max_profit(prices):
    result = prices[1] - prices[0]
    m = prices[0]
    for x in islice(prices, 1, None):
        result = max(x-m, result)
        m = min(x, m)
    return result
