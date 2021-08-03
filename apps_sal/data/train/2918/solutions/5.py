def nbMonths(priceOld, priceNew, savingMonth, percentLoss):
    if priceOld > priceNew:
        return [0, priceOld - priceNew]
    months = 0
    savings = 0
    loss = percentLoss / 100
    while savings + priceOld < priceNew:
        months += 1
        savings += savingMonth
        if months % 2 == 0:
            loss += 0.005
        priceOld -= priceOld * loss
        priceNew -= priceNew * loss
    saved = round(savings + priceOld - priceNew)
    return [months, saved]
