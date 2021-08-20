def fuel_price(litres, price_per_liter):
    return round(litres * (price_per_liter - min(25, litres / 2 * 5) / 100), 2)
