def fuel_price(litres, price_per_litre):
    if litres < 2:
        return litres * price_per_litre
    elif litres < 4:
        return litres * (price_per_litre - 0.05)
    elif litres < 6:
        return litres * (price_per_litre - 0.1)
    elif litres < 8:
        return litres * (price_per_litre - 0.15)
    elif litres < 10:
        return litres * (price_per_litre - 0.2)
    else:
        return litres * (price_per_litre - 0.25)
