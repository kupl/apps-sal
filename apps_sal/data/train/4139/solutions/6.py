def rental_car_cost(d):
    total = d * 40
    if d >= 7:
        total -= 50
    elif d >= 3:
        total -= 20
    return total
