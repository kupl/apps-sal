def rental_car_cost(d):
    prod = d * 40
    return prod - 30 * (d >= 7) - 20 * (d >= 3)
