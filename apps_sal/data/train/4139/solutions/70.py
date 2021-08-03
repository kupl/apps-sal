def rental_car_cost(d):
    x = 40 * d
    if d >= 3:
        if d >= 7:
            return x - 50
        return x - 20
    return x
