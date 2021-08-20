def fuel_price(litres, price_per_liter):
    discount = litres // 2 * 0.05
    discount = discount if discount <= 0.25 else 0.25
    return round(litres * price_per_liter - litres * discount, 2)
