def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    i = 0
    while savingperMonth * i + startPriceOld < startPriceNew:
        if i % 2:
            percentLossByMonth += 0.5
        startPriceOld -= startPriceOld * 0.01 * percentLossByMonth
        startPriceNew -= startPriceNew * 0.01 * percentLossByMonth
        i += 1
    return [i, round(savingperMonth * i + startPriceOld - startPriceNew)]
