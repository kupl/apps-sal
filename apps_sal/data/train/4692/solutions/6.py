def max_profit(prices):
    low = prices[0]
    profit = prices[1] - low
    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - low)
        low = min(low, prices[i])
    return profit
