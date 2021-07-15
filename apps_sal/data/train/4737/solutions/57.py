def fuel_price(litres, price_per_liter):
    discount_per_liter = min((litres // 2) * 0.05, 0.25)
    return litres * price_per_liter - litres * discount_per_liter

