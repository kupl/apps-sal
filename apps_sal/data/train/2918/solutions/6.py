def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    months_elapsed = 0
    if startPriceOld >= startPriceNew:
        return [months_elapsed, startPriceOld - startPriceNew]

    too_poor = True
    while too_poor:
        months_elapsed += 1

        if months_elapsed % 2 == 0:
            percentLossByMonth += 0.5

        startPriceOld = startPriceOld * (1 - (percentLossByMonth / 100))
        startPriceNew = startPriceNew * (1 - (percentLossByMonth / 100))
        available_funds = (startPriceOld + (savingperMonth * months_elapsed))

        if available_funds >= startPriceNew:
            too_poor = False

    return [months_elapsed, int(round(available_funds - startPriceNew))]
