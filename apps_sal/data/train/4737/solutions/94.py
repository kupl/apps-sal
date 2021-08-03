def fuel_price(litres, price_per_liter):
    if litres >= 10:
        return litres * (price_per_liter - 0.25)
    if litres >= 8:
        return litres * (price_per_liter - 0.20)
    if litres >= 6:
        return litres * (price_per_liter - 0.15)
    if litres >= 4:
        return litres * (price_per_liter - 0.10)
    if litres >= 2:
        return litres * (price_per_liter - 0.05)
