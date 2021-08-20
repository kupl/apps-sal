def fuel_price(litres, price_per_liter):
    resultat = 0
    if litres < 2:
        resultat = litres * price_per_liter
    elif litres < 4:
        resultat = litres * (price_per_liter - 0.05)
    elif litres < 6:
        resultat = litres * (price_per_liter - 0.1)
    elif litres < 8:
        resultat = litres * (price_per_liter - 0.15)
    elif litres < 10:
        resultat = litres * (price_per_liter - 0.2)
    else:
        resultat = litres * (price_per_liter - 0.25)
    return float('{0:.2f}'.format(resultat))
