def profitLoss(r):
    return round(sum((i[0] - i[0] * 100.0 / (100 + i[1]) for i in r)), 2)
