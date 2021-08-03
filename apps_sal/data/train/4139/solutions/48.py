def rental_car_cost(d):
    result = 40 * d
    if 3 <= d < 7:
        result -= 20
    elif d >= 7:
        result -= 50
    return result
