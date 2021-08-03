def rental_car_cost(d):
    x = d * 40
    if d >= 7:
        x = x - 50
    elif d in range(3, 7):
        x = x - 20
    return x
