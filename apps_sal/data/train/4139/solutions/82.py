def rental_car_cost(d):
    print(d)
    if d <= 2:
        return 40 * d
    if 2 < d < 7:
        return 40 * d - 20
    if d >= 7:
        return d * 40 -50# your code
