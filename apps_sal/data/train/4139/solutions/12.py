def rental_car_cost(d):
    x = d * 40
    if d >= 7:
        return x - 50
    return x - 20 if d >= 3 else x
