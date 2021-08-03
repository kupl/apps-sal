def profitLoss(records):
    return round(100 * (sum(c[0] - c[0] / (1 + c[1] / 100) for c in records))) / 100
