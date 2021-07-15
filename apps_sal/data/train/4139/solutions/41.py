def rental_car_cost(days):
    if days >= 7:
        discount = 50
    elif days >= 3:
        discount = 20
    else:
        discount = 0
    return days * 40 - discount
