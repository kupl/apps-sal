def fuel_price(litres, price_per_litre):
    return litres * max(price_per_litre - 0.25, price_per_litre - 0.05 * (litres // 2))
