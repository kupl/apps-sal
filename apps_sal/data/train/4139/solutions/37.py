def rental_car_cost(d):
    return d * 40 if d <= 2 else d * 40 -20 if d <= 6 else d * 40 - 50
