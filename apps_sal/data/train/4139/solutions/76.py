def rental_car_cost(d):
    return 40 * d - (d > 6) * 30 - (d > 2) * 20
