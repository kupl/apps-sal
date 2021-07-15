def rental_car_cost(d):
    return d * 40 - (d >= 3) * 20 - (d >= 7) * 30
