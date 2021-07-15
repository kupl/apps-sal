def fuel_price(litres, price_per_liter):
    discount_price = 0.05 * (litres // 2)
    if discount_price > 0.25:
        discount_price = 0.25
    return round(litres * (price_per_liter - discount_price), 2)
