def rental_car_cost(d):
    rent = d * 40
    if d >= 7:
        rent -= 50
    elif d >= 3 and d < 7:
        rent -= 20
    return rent
