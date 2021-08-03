def fuel_price(litres, price_per_litre):
    return round(litres * (price_per_litre - min(0.05 * (litres // 2), 0.25)), 2)
