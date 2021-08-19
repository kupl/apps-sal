def fuel_price(litres, price_per_liter):
    if litres >= 2:
        d = litres * 0.05
    if litres >= 4:
        d = litres * 0.1
    if litres >= 6:
        d = litres * 0.15
    if litres >= 8:
        d = litres * 0.2
    if litres >= 10:
        d = litres * 0.25
    return litres * price_per_liter - d
