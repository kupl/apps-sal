def rental_car_cost(d):
    if d < 3:
        a = d * 40
        return a
    elif d >= 3 and d < 7:
        b = d * 40 - 20
        return b
    elif d >= 7:
        c = d * 40 - 50
        return c
