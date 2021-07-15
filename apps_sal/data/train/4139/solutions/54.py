def rental_car_cost(d):
    amount = 40 * d
    if d >= 7:
        amount -= 50
    elif d >= 3:
        amount -= 20
    return amount
