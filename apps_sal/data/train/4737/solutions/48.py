def fuel_price(litres, price_per_liter):
    return litres*price_per_liter-min(0.05*(litres//2),0.25)*litres
