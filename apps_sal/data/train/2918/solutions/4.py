def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    total=0
    count=0
    while total+startPriceOld<startPriceNew:
        count+=1
        if count and count%2==0:
            percentLossByMonth+=0.5
        startPriceOld=startPriceOld*(100-percentLossByMonth)/100
        startPriceNew=startPriceNew*(100-percentLossByMonth)/100
        total+=savingperMonth
    return [count, round(total+startPriceOld-startPriceNew)]
