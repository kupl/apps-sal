def max_profit(prices):
    (save, best) = (float('inf'), float('-inf'))
    for p in prices:
        best = max(best, p - save)
        save = min(save, p)
    return best
