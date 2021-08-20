def fuel_price(litres, price_per_liter):
    discount = litres // 2 * 0.05
    if litres >= 10:
        discount = 0.25
    total = round((price_per_liter - discount) * litres, 2)
    return total
