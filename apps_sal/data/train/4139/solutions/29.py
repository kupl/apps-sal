def rental_car_cost(d):
    # your code
    return 40 * d - 20 * (d < 7 and d >= 3) - 50 * (d >= 7)
