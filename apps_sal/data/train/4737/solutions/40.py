def fuel_price(litres, price_per_liter):

    if litres >= 2 and litres < 4:
        cost = (price_per_liter - 0.05) * litres
    elif litres >= 4 and litres < 6:
        cost = (price_per_liter - 0.10) * litres
    elif litres >= 6 and litres < 8:
        cost = (price_per_liter - 0.15) * litres
    elif litres >= 8 and litres < 10:
        cost = (price_per_liter - 0.20) * litres
    else:
        cost = (price_per_liter - 0.25) * litres
    return round(cost, 2)
