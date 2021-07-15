def rental_car_cost(d):
    return d * 40 - (d > 6) * 50 - (7 > d > 2) * 20
