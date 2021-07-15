def fuel_price(litres, price_per_litre):
    return litres * price_per_litre - ((2 <= litres < 4) * 0.05 * litres) - ((4 <= litres < 6) * 0.1 * litres) - ((6 <= litres < 8) * 0.15 * litres) - ((8 <= litres < 10) * 0.2 * litres) - ((10 <= litres) * 0.25 * litres)
