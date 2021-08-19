def fuel_price(litres, price_per_liter):
    return round(litres * (price_per_liter - min(litres // 2 * 0.05, 0.25)), 2)
