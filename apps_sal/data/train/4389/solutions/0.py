def profitLoss(records):
    return round(sum((price - price / (1 + profit / 100) for (price, profit) in records)), 2)
