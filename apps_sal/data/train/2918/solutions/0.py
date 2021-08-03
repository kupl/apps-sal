def nbMonths(oldCarPrice, newCarPrice, saving, loss):
    months = 0
    budget = oldCarPrice

    while budget < newCarPrice:
        months += 1
        if months % 2 == 0:
            loss += 0.5

        oldCarPrice *= (100 - loss) / 100
        newCarPrice *= (100 - loss) / 100
        budget = saving * months + oldCarPrice

    return [months, round(budget - newCarPrice)]
