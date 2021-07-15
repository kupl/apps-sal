def rental_car_cost(d):
    daily_cost = (d * 40)
    if d >= 3 and d < 7:
        #three_day_reduced_cost = daily_cost - 20
        return daily_cost - 20
    elif d >= 7:
       # seven_day_reduced_cost = daily_cost - 50
        return daily_cost - 50 
    else:
        return daily_cost
