def rental_car_cost(d):
    if d >= 3 and d < 7:
        total = d * 40 - 20
        return total
    elif d >= 7:
        total = d * 40 - 50
        return total
    else:
        total = d * 40
        return d * 40
    # your code
