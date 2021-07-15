def fuel_price(litres, price_per_liter):
    return round(litres * (price_per_liter - {0: 0, 1: .05, 2: .10, 3: .15, 4: .20}.get(litres // 2, .25)), 2)
