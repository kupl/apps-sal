def fuel_price(litres, price_per_litre):
    discount = min(25, litres // 2 * 5)
    price = litres * price_per_litre - discount * litres / 100
    return round(price, 2)
