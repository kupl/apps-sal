import math


def duty_free(price, discount, holiday_cost):
    """(^-__-^)"""
    count_bottle = (price / 100) * discount
    result = holiday_cost / count_bottle
    return (math.floor(result))
