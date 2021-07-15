def rental_car_cost(d):
    price = d * 40
    if d >= 7:
        price -= 50
    elif d >= 3 and d < 7:
        price -= 20
    return price
