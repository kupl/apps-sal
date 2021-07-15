def fuel_price(litres, price_per_liter):
    print(litres, price_per_liter)
    return litres * price_per_liter - min((litres // 2) * 0.05, 0.25) * litres
