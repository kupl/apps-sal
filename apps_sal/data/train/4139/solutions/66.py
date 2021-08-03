def rental_car_cost(d):
    total = d * 40
    if 3 <= d < 7:
        total -= 20
    if 7 <= d:
        total -= 50
    return total
