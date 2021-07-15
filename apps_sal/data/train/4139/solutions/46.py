def rental_car_cost(d):
    suma = d * 40
    if d < 3:
        return suma
    elif d >= 3 and d < 7:
        return suma - 20
    elif d >= 7:
        return suma - 50
