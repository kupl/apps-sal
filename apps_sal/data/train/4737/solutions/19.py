def fuel_price(litres, price_per_litre):
    if litres > 0 and price_per_litre > 0:
        if 2 <= litres < 4:
            price_per_litre_real = price_per_litre - 0.05
        elif 4 <= litres < 6:
            price_per_litre_real = price_per_litre - 0.1
        elif 6 <= litres < 8:
            price_per_litre_real = price_per_litre - 0.15
        elif 8 <= litres < 10:
            price_per_litre_real = price_per_litre - 0.2
        elif 10 <= litres:
            price_per_litre_real = price_per_litre - 0.25
        return litres * price_per_litre_real
