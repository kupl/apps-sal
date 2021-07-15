def rental_car_cost(d):
    total_cost = d * 40
    if d >= 7:
        total_cost -= 50
    elif d >= 3:
        total_cost -= 20
    return total_cost
