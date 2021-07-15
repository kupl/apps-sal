def rental_car_cost(d):
    car = 40
    if d < 3:
        return car * d
    if 3 <= d < 7:
        return car * d - 20
    if 7 <= d:
        return car * d - 50
