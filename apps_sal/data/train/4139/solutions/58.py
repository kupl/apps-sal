def rental_car_cost(d):
    daily_cost = 40 * d
    if d >= 7:
        daily_cost -= 50
    elif d >= 3:
        daily_cost -= 20
    else:
        daily_cost -= 0
    return daily_cost
