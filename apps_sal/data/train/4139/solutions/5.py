def rental_car_cost(d):
    return d * 40 - 20 * (d >= 3) - 30 * (d >= 7)
