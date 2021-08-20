def rental_car_cost(d):
    return d * 40 - (0 if d < 3 or d > 6 else 20) - (0 if d < 7 else 50)
