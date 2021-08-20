def rental_car_cost(d):
    if d == 1:
        return 40
    elif d >= 7:
        a = d * 40
        return a - 50
    elif 3 <= d < 7:
        a = d * 40
        return a - 20
    else:
        return d * 40
