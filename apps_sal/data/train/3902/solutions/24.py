from math import *

def duty_free(price, discount, holiday_cost):
    discount_multiplyer = discount / 100
    return floor(holiday_cost / (price*discount_multiplyer))
