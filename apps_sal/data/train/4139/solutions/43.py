def rental_car_cost(d):
    count = 40
    if d >= 1 and d < 3:
        count = count * d
    elif d >= 3 and d < 7:
        count = count * d - 20
    elif d >= 7:
        count = count * d - 50
    return count
