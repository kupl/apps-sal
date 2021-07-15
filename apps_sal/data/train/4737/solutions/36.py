def fuel_price(litres, price_per_litre):
    print(litres, price_per_litre)
    suma = litres * price_per_litre
    if litres >= 2 and litres < 4:
        return round(suma - (0.05 * litres), 2)
    if litres >= 4 and litres < 6:
        return round(suma - (0.10 * litres), 2)
    if litres >= 6 and litres < 8:
        return round(suma - (0.15 * litres), 2)
    if litres >= 8 and litres < 10:
        return round(suma - (0.20 * litres), 2)
    if litres >= 10:
        return round(suma - (0.25 * litres), 2)
