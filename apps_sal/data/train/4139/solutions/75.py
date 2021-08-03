def rental_car_cost(d):
    p = d * 40
    if d < 3:
        return p
    elif d < 7:
        return p - 20
    else:
        return p - 50
