def fuel_price(litres, price_per_liter):
    if 0 < litres < 2:
        return price_per_liter * litres
    elif 4 > litres >= 2:
        return round((price_per_liter - .05) * litres, 2)
    elif 6 > litres >= 4:
        return round((price_per_liter - .10) * litres, 2)
    elif 8 > litres >= 6:
        return round((price_per_liter - .15) * litres, 2)
    elif 10 > litres >= 8:
        return round((price_per_liter - .20) * litres, 2)
    elif litres >= 10:
        return round((price_per_liter - .25) * litres, 2)
