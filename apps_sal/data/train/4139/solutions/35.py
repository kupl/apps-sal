def rental_car_cost(d):
    if d < 3:
        x = 0
    elif d < 7:
        x = 20
    else:
        x = 50
    return d * 40 - x
