import math
def duty_free(price, discount, holiday_cost):
    return round(int(holiday_cost/(discount*(price/100))))
