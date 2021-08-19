def fuel_price(litres, price_per_liter):
    price_per_liter -= min(0.25, 0.05 * (litres // 2))
    return round(litres * price_per_liter, 2)
