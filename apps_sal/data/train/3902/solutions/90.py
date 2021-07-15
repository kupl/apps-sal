def duty_free(price, discount, holiday_cost):
    savings = price * (discount /100)
    bottles = 0
    suma = savings
    while suma < holiday_cost:
        bottles += 1
        suma += savings
    return bottles

