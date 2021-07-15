def fuel_price(litres, price_per_liter):
    if litres >= 10:
        price = litres * (price_per_liter - 0.25)
    else:
        price = litres * (price_per_liter - 0.05 * (litres // 2))
    return round(price, 2)
