def duty_free(price, discount, holiday_cost):
    x = price * (discount * 0.01)
    return int(holiday_cost / x)
