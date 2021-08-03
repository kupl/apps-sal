def fuel_price(litres, price_per_liter):
    if 2 <= litres < 4:
        return round(litres * (price_per_liter - 0.05), 2)
    if 4 <= litres < 6:
        return round(litres * (price_per_liter - 0.1), 2)
    if 6 <= litres < 8:
        return round(litres * (price_per_liter - 0.15), 2)
    if 8 <= litres < 10:
        return round(litres * (price_per_liter - 0.2), 2)
    if litres >= 10:
        return round(litres * (price_per_liter - 0.25), 2)
