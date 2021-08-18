def rental_car_cost(d):
    if 0 < d < 3:
        return 40 * d
    if 2 < d < 7:
        return 40 * d - 20
    if d > 6:
        return 40 * d - 50
