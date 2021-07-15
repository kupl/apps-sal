def fuel_price(litres, price_per_liter):
    if 0<litres<=10:
        p=(0.05*(litres//2))
    else:
        p=0.25
    return litres*price_per_liter - litres*p
