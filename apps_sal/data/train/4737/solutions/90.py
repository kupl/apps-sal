def fuel_price(litres, price_per_liter):
    if litres >= 10:
        return round(litres * (price_per_liter - 0.25), 2)
    if litres >= 8:
        return round(litres * (price_per_liter - 0.20), 2)
    if litres >= 6:
        return round(litres * (price_per_liter - 0.15), 2)
    if litres >= 4:
        return round(litres * (price_per_liter - 0.10), 2)
    if litres >= 2:
        return round(litres * (price_per_liter - 0.05), 2)
    if litres < 2:
        return round(litres * price_per_liter, 2)
