def rental_car_cost(d):
    total = d * 40
    if d >= 3 and d < 7:
        total -= 20
    if d >= 7:
        total -= 50
    return total
