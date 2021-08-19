def fuel_price(litres, price_per_liter):
    disc = litres // 2 * 0.05
    if disc > 0.25:
        disc = 0.25
    price_per_liter -= disc
    total = price_per_liter * litres
    return round(total, 2)
