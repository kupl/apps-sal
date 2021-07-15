def fuel_price(liters, price_per_liter):
    discount = min(.25, .05 * (liters // 2)) * liters
    return (liters * price_per_liter) - discount
