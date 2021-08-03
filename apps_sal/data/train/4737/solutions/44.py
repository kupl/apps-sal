def fuel_price(litres, price_per_liter):
    litres_div2 = litres // 2
    if litres_div2 <= 5:
        return round(litres * (price_per_liter - litres_div2 * .05), 2)
    discount = 2.5 + (litres - 10) * .25
    return round(litres * price_per_liter - discount, 2)
