def rental_car_cost(d):

    sum = 40*d
    
    if d >= 7:
        sum = sum - 50
        
    elif d >= 3:
        sum = sum - 20
        
    return sum
