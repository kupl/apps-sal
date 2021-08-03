def rental_car_cost(d):
    print(d)
    total = 40 * d
    if d >= 7:
        return total - 50
    elif d < 3:
        return total
    return total - 20
