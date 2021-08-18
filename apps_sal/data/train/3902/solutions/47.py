def duty_free(price, discount, holiday_cost):
    money = price * (discount / 100)
    return int(holiday_cost / money)
