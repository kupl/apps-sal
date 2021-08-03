def fuel_price(litres, price_per_liter):
    if 0 < litres < 2:
        return round(litres * price_per_liter, 2)
    elif 2 <= litres < 4:
        return round(litres * (price_per_liter - 0.05), 2)
    elif 4 <= litres < 6:
        return round(litres * (price_per_liter - 0.10), 2)
    elif 6 <= litres < 8:
        return round(litres * (price_per_liter - 0.15), 2)
    elif 8 <= litres < 10:
        return round(litres * (price_per_liter - 0.20), 2)
    elif litres >= 10:
        return round(litres * (price_per_liter - 0.25), 2)
