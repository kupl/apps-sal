def rental_car_cost(d):
    t = d * 40
    if d >= 3 and d < 7:
        t = t - 20
    if d >= 7:
        t = t - 50
    return t
