import math


def duty_free(price, discount, holiday_cost):
    x = holiday_cost / (price - (price - (price * (discount / 100))))
    return math.floor(x)
