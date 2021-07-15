def fuel_price(litres, price_per_liter):
    discount = 0
    if(litres >= 2):
        discount = 0.05
    if(litres >= 4):
        discount = 0.1
    if(litres >= 6):
        discount = 0.15
    if(litres >= 8):
        discount = 0.2
    if(litres >= 10):
        discount = 0.25
    total = litres * price_per_liter - litres * discount
    return total
