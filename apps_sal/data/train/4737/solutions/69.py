def fuel_price(litres, price_per_liter):
    discount = litres // 2 * 0.05
    discount = 0.25 if discount >= 0.25 else discount
    return round(litres * (price_per_liter - discount), 2)
