def fuel_price(litres, price_per_litre):
    if litres < 2:
        price = litres * price_per_litre
    elif litres < 4:
        price = litres * (price_per_litre - 0.05)
    elif litres < 6:
        price = litres * (price_per_litre - 0.10)
    elif litres < 8:
        price = litres * (price_per_litre - 0.15)
    elif litres < 10:
        price = litres * (price_per_litre - 0.20)
    else:
        price = litres * (price_per_litre - 0.25)
    price = round(price, 2)
    return price
