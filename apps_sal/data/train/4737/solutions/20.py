def fuel_price(litres, price_per_litre):
    total_price = 0
    price_per_litre = float(price_per_litre)
    for x in range(litres):
        if litres < 4:
            total_price += price_per_litre
        elif litres < 6:
            total_price += price_per_litre - 0.05
        elif litres < 8:
            total_price += price_per_litre - 0.15
        elif litres < 10:
            total_price += price_per_litre - 0.2
        else:
            total_price += price_per_litre - 0.25
    return round(float(total_price), 2)
