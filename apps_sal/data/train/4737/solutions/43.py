def fuel_price(litres, price_per_liter):
    d = litres // 2 * 0.05 if litres <= 10 else 0.25
    return round(litres * (price_per_liter - d), 2)
