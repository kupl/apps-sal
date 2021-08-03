import math


def duty_free(price, discount, holiday_cost):
    actual_discount = (discount / 100) * price
    no_of_bottles = holiday_cost / actual_discount
    return math.floor(no_of_bottles)
