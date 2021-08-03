def fuel_price(litres, price_per_liter):
    price = price_per_liter * litres
    if litres >= 10:
        price = price - (litres * 0.25)
    elif litres >= 8:
        price = price - (litres * 0.20)
    elif litres >= 6:
        price = price - (litres * 0.15)
    elif litres >= 4:
        price = price - (litres * 0.10)
    elif litres >= 2:
        price = price - (litres * 0.05)
    else:
        return price
    return price
