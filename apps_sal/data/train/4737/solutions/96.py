def fuel_price(litres, price_per_liter):
    if 2 <= litres < 4:
        price_per_liter -= 0.05
    elif 4 <= litres < 6:
        price_per_liter -= 0.1
    elif 6 <= litres < 8:
        price_per_liter -= 0.15
    elif 8 <= litres < 10:
        price_per_liter -= 0.2
    elif litres >= 10:
        price_per_liter -= 0.25
    return round(litres * price_per_liter, 2)
