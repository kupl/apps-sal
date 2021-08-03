def fuel_price(litres, price_per_litre):
    if litres >= 10:
        price_per_litre = price_per_litre - 0.25
    elif litres >= 8:
        price_per_litre = price_per_litre - 0.20
    elif litres >= 6:
        price_per_litre = price_per_litre - 0.15
    elif litres >= 4:
        price_per_litre = price_per_litre - 0.10
    elif litres >= 2:
        price_per_litre = price_per_litre - 0.05

    return litres * price_per_litre
