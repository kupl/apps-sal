def fuel_price(litres, price_per_litre):
    if litres < 2:
        return litres * price_per_litre
    elif litres < 4:
        return litres * (price_per_litre - .05)
    elif litres < 6:
        return litres * (price_per_litre - .10)
    elif litres < 8:
        return litres * (price_per_litre - .15)
    elif litres < 10:
        return litres * (price_per_litre - .20)
    else:
        return litres * (price_per_litre - .25)
