def profitLoss(records):
    return round(sum(pr * pe / (100 + pe) for pr, pe in records), 2)
