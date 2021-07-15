def fuel_price(litres, price_per_litre):
    if litres > 9:
        return round(litres*(price_per_litre-0.25), 2)
    elif litres > 7:
        return round(litres*(price_per_litre-0.20), 2)
    elif litres > 5: 
        return round(litres*(price_per_litre-0.15), 2)
    elif litres > 3: 
        return round(litres*(price_per_litre-0.10), 2)
    elif litres > 1: 
        return round(litres*(price_per_litre-0.05), 2)
    else:
        return litres*(price_per_litre)
