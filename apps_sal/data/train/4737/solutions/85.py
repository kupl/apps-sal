def fuel_price(litres, price_per_liter):
    discount = litres // 2 * 0.05 if litres // 2 < 6 else 0.25
    return price_per_liter * litres - discount * litres
