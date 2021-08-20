def rental_car_cost(d):
    if d >= 7:
        tot = 40 * d - 50
    elif d >= 3:
        tot = 40 * d - 20
    else:
        tot = 40 * d
    return tot
