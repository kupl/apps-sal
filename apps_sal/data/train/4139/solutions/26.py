def rental_car_cost(d):
    cost = 40
    if int(d)<3:
        cost = cost * d
    elif int(d)>=3 and int(d)<7:
        cost = cost * d 
        cost = cost - 20
    elif int(d)>=7:
        cost = cost * d
        cost = cost -50
    return cost
