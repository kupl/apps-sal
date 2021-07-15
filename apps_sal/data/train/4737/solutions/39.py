def fuel_price(litres, price_per_liter):
    if litres>=5:
        return round(litres*(price_per_liter-0.25),2)

