def fuel_price(litres, price_per_litre):
    discount = min(litres // 2 * 5, 25) * 0.01
    return round(litres * (price_per_litre - discount), 2)

