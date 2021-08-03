import math


def duty_free(price, discount, holiday_cost):
    leftover = price * (discount / 100)
    num = holiday_cost / leftover
    return math.floor(num)
