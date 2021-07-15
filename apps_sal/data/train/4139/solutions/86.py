def rental_car_cost(d):
    daily = d * 40
    if d < 7 and d > 2:
        return daily - 20
    elif d > 6:
        return daily - 50
    else:
        return daily

