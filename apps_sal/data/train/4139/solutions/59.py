def rental_car_cost(d):
    price = d * 40
    
    return price if d < 3 else price - 50 if d >= 7 else price - 20
