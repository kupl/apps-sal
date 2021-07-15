def rental_car_cost(d):
    off = 50 if d > 6 else 20 if d > 2 else 0
    return 40 * d - off
