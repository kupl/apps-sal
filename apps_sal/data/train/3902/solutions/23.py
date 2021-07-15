import math

def duty_free(price, discount, holiday_cost):
    percent = discount / 100 * price
    bottles = holiday_cost / percent
    return math.floor(bottles)
