def rental_car_cost(d):
    if 0 < d < 3:
        return d * 40
    elif 2 < d < 7:
        return d * 40 - 20
    else:
        return 40 * d - 50
