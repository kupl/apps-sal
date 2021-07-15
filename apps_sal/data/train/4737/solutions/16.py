def fuel_price(litres, price_per_litre):
    return litres * (price_per_litre - 0.25) if litres >= 10 else round(litres * (price_per_litre - (litres // 2 * 5) / 100), 2)
