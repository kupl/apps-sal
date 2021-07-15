def rental_car_cost(d):
    cpd = 40
    if d < 3:
        return d * cpd
    elif d < 7:
        return (d * cpd) - 20
    else:
        return (d * cpd) - 50
