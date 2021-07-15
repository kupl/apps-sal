def duty_free(price, discount, holiday_cost):
    bottles = holiday_cost / (price * discount)
    return int(bottles * 100)
