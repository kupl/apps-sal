def rental_car_cost(d):
    fuckthis = 40 * d
    if 3 <= d < 7:
        return fuckthis - 20
    elif d >= 7:
        return fuckthis - 50
    else:
        return fuckthis
