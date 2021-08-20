def fuel_price(litres, price_per_liter):
    if litres >= 10:
        price_per_liter -= 0.25
        return round(litres * price_per_liter, 2)
    elif litres >= 8:
        price_per_liter -= 0.2
        return round(litres * price_per_liter, 2)
    elif litres >= 6:
        price_per_liter -= 0.15
        return round(litres * price_per_liter, 2)
    elif litres >= 4:
        price_per_liter -= 0.1
        return round(litres * price_per_liter, 2)
    elif litres >= 2:
        price_per_liter -= 0.05
        return round(litres * price_per_liter, 2)
    elif litres < 2:
        return round(litres * price_per_liter, 2)
