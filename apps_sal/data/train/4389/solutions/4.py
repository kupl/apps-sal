def profitLoss(records):
    return round(sum(x * p / (100 + p) for x, p in records), 2)
