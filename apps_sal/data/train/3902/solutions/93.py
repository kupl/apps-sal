def duty_free(price, discount, holiday_cost):
    count = holiday_cost // (price * discount / 100)
    return count
