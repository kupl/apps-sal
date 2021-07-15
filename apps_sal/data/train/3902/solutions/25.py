import math
def duty_free(price, discount, holiday_cost):
    discount = discount * .01
    savings_per_bottle = price * discount
    number_of_bottles_needed = holiday_cost / savings_per_bottle
    return math.floor(number_of_bottles_needed)
