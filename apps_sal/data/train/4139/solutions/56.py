def rental_car_cost(d):
    return 40 * d - [0, 20, 50][(d > 2) + (d > 6)]
