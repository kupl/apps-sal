def rental_car_cost(d):
    return d * 40 - (d > 6 and 50 or (d > 2 and 20) or 0)
