def rental_car_cost(d):
    r = d * 40
    if d >= 7:
        r -= 50
    elif d >= 3:
        r -= 20
    return r
