def rental_car_cost(d):
    return d * 40 - (d >= 7) * 50 - (3 <= d < 7) * 20
