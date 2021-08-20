def fuel_price(litres, price_per_liter):
    return litres * (price_per_liter - 0.25) if litres >= 10 else litres * (price_per_liter - 0.1) if litres >= 4 else litres * (price_per_liter - 0.05)
