def rental_car_cost(d):
    return 40 * d - 50 * (d > 6) if d > 6 else 40 * d - 20 * (d > 2)
