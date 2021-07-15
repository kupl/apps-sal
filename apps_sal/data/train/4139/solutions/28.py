def rental_car_cost(d):
    return d * 40 - (20 if d >= 3 else 0) - (30 if d >= 7 else 0)
