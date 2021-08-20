def fuel_price(litres, price_per_liter):
    return litres * max(price_per_liter - 0.25, price_per_liter - 0.05 * (litres // 2))
