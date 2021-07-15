def rental_car_cost(d):
    days = d * 40
    if d >= 7:
        days -= 50
    if d >= 3 and d < 7:
        days -= 20
    return days
