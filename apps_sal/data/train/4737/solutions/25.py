def fuel_price(litres, price_per_litre):

    if litres < 2:
        return round(price_per_litre * litres, 2)
    elif 2 <= litres < 4:
        return round((price_per_litre * litres) - (.05 * litres), 2)
    elif 4 <= litres < 6:
        return round((price_per_litre * litres) - (.10 * litres), 2)
    elif 6 <= litres < 8:
        return round((price_per_litre * litres) - (.15 * litres), 2)
    elif 8 <= litres < 10:
        return round((price_per_litre * litres) - (.20 * litres), 2)
    else:
        return round((price_per_litre * litres) - (.25 * litres), 2)
