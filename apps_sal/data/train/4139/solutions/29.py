def rental_car_cost(d):
    return 40 * d - 20 * (d < 7 and d >= 3) - 50 * (d >= 7)
