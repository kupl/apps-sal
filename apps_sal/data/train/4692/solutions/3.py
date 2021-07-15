def max_profit(prices):
    mini, best = prices[0], -prices[0]
    for price in prices[1:]:
        best = max(best, price - mini)
        mini = min(mini, price)
    return best
