def rental_car_cost(d):
    if d<3:
        return 40*d
    elif d in range(3,7):
        return 40*d-20
    else:
        return 40*d-50
