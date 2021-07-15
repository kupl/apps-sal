def rental_car_cost(d):
    x = 40
    if d < 3: 
        return d * x
    elif d < 7: 
        return (x * d) - 20
    else: 
        return (x * d) - 50 
