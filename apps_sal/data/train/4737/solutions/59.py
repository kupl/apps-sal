def fuel_price(litres, price_per_liter):
    return litres * (price_per_liter - (0.01* (5*litres/2 if litres % 2 == 0 else 5*(litres -1)/2) if litres <=10 else 0.25))
