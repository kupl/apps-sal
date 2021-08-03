def rental_car_cost(d):
    base = d * 40
    if d >= 7:
        return base - 50
    elif d >= 3:
        return base - 20
    else:
        return base
