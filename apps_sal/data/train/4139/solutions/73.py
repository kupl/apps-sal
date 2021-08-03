def rental_car_cost(d):
    if d < 7:
        if d >= 3:
            return d * 40 - 20
        return d * 40
    return d * 40 - 50
