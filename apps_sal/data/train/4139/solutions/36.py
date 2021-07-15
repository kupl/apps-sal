def rental_car_cost(d):
    return 40 * d - 50 if d > 6 else 40 * d - 20 if 3 <= d <= 6 else 40 * d
