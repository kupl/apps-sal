def rental_car_cost(d):
    _1_day = d*40
    if d >= 7:
        _1_day -=50
    elif d >= 3:
        _1_day -=20
    return _1_day
