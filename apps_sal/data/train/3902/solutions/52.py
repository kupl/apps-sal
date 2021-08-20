import math


def duty_free(price, discount, holiday_cost):
    percent = price / 100 * discount
    return math.floor(holiday_cost / percent)


print(duty_free(12, 50, 1000))
