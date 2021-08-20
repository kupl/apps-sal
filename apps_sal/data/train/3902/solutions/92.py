import math


def duty_free(price, discount, holiday_cost):
    x = price * (discount / 100)
    return math.floor(holiday_cost / x)
