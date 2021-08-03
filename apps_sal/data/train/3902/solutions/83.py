def duty_free(price, discount, holiday_cost):
    saved_money = price * (discount / 100)
    return int(holiday_cost / saved_money)
