import math


def duty_free(price, discount, holiday_cost):
    i = discount / 100 * price
    return math.floor(holiday_cost / i)
