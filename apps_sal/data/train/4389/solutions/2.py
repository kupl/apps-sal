def profitLoss(records):

    return round(sum(amount * (1 - 1 / (1 + perc / 100)) for amount, perc in records), 2)
