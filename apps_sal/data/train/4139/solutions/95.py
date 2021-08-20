def rental_car_cost(d):
    if d < 3:
        return d * 40
    elif d < 7 and d >= 3:
        return d * 40 - 20
    elif d >= 7:
        return d * 40 - 50
