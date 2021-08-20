def rental_car_cost(d):
    cost = 40 * d
    print(d)
    if d >= 3 and (not 7 <= d):
        cost -= 20
    if d >= 7:
        cost -= 50
    return cost
