def fuel_price(litres, price_per_liter):
    discount = 0
    if 2 <= litres < 4:
        discount = 0.05
    elif 4 <= litres < 6:
        discount = 0.1
    elif 6 <= litres <= 8:
        discount = 0.2
    elif 8 < litres:
        discount = 0.25
    print(litres, price_per_liter, discount)
    return litres * price_per_liter - litres * discount
