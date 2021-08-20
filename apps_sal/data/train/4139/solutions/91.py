def rental_car_cost(d):
    dayCost = 40
    if d >= 3 and d < 7:
        return dayCost * d - 20
    elif d >= 7:
        return dayCost * d - 50
    return d * dayCost
