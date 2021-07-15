def rental_car_cost(d):
    if d < 3:
        return 40 * d
    else:
        return 40 * d - 20 if d < 7 else 40 * d - 50

