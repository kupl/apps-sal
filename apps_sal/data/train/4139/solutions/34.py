def rental_car_cost(d):
    return d * 40 if d < 3 else d * 40 - 20 if 2 < d < 7 else d * 40 - 50
