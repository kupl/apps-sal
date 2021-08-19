def fuel_price(litres, price_per_liter):
    if litres < 2:
        price = litres * price_per_liter
    elif litres < 4:
        price = litres * (price_per_liter - 0.05)
    elif litres < 6:
        price = litres * (price_per_liter - 0.1)
    elif litres < 8:
        price = litres * (price_per_liter - 0.15)
    elif litres < 10:
        price = litres * (price_per_liter - 0.2)
    else:
        price = litres * (price_per_liter - 0.25)
    return round(price, 2)
