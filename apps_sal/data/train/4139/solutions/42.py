def rental_car_cost(d):
    rent_cost = d*40
    if d >= 7:
        rent_cost-=50
    elif d >= 3:
        rent_cost-=20
    return rent_cost     


