def profitLoss(records):
    return round(sum((price * percent / (100 + percent) for (price, percent) in records)), 2)
