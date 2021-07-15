def fuel_price(litres, price_per_liter):
    return round(litres * (price_per_liter - .05 * min(litres // 2, 5)), 2)
