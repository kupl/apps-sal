def rental_car_cost(d):
    print(d,"days",d*40)
    return (d*40)-50 if d >= 7 else (d*40)-20 if d < 7 and d >= 3 else (d*40)
