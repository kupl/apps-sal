def fuel_price(litres, price_per_liter):
    return round(litres * (price_per_liter - {0: 0, 1: 0.05, 2: 0.1, 3: 0.15, 4: 0.2}.get(litres // 2, 0.25)), 2)
