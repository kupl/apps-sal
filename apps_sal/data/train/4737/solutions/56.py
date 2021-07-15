def fuel_price(litres, price_per_liter):
    discount = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25][(litres >= 2) + (litres >= 4) + (litres >= 6) + (litres >= 8) + (litres >= 10)]
    return litres * price_per_liter - discount * litres
