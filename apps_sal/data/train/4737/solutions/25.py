def fuel_price(litres, price_per_litre):
    if litres < 2:
        return round(price_per_litre * litres, 2)
    elif 2 <= litres < 4:
        return round(price_per_litre * litres - 0.05 * litres, 2)
    elif 4 <= litres < 6:
        return round(price_per_litre * litres - 0.1 * litres, 2)
    elif 6 <= litres < 8:
        return round(price_per_litre * litres - 0.15 * litres, 2)
    elif 8 <= litres < 10:
        return round(price_per_litre * litres - 0.2 * litres, 2)
    else:
        return round(price_per_litre * litres - 0.25 * litres, 2)
