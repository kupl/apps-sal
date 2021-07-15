def rental_car_cost(d):
    total = 40 * d
    if d > 6:
        total = total - 50
    if d > 2 and d < 7:
        total = total - 20
    return total
