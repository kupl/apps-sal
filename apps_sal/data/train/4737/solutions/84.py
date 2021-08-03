def fuel_price(litres, price_per_liter):
    raw_discount = 0.05 * (litres / 2)
    discount = 0.25 if raw_discount > 0.25 else raw_discount
    return round(litres * (price_per_liter - discount), 2)
