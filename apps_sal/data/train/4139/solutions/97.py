def discount(d):
    if d >= 7:
        return 50
    elif d >= 3:
        return 20
    return 0


def rental_car_cost(d):
    return d*40 - discount(d)

