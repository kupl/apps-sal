def rental_car_cost(d):
    total = 40*d
    return total if d < 3 else total-20 if d < 7 else total-50
