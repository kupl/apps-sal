def fuel_price(litres, price_per_liter):
    price_per_liter_with_discount = price_per_liter
    i = 2
    while i <= 10:
        if litres >= i:
            price_per_liter_with_discount -= 0.05
        i += 2
    return round(litres * price_per_liter_with_discount, 2)
