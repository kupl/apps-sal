def profitLoss(records):
    return round(sum([r - (r / (1 + p / 100)) for r, p in records]), 2)

