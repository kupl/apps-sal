import math

def duty_free(price, discount, holiday_cost):
    save = price*(discount/100)
    price = holiday_cost/save
    return math.floor(price)
