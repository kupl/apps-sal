def profitLoss(records):
    return round(sum(map(lambda r: r[0] * r[1] / (100 + r[1]), records)), 2)
