def fuel_price(litres, price_per_liter):
    if litres <= 1:
        return price_per_liter * litres
    dis = litres // 2 * 0.05
    if dis <= 0.25:
        return round(litres * (price_per_liter - dis), 2)
    else:
        return round(litres * (price_per_liter - 0.25), 2)
