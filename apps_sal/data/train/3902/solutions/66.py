def duty_free(price, discount, holiday_cost):
    x = price * (discount / 100)
    price = holiday_cost / x
    return int(price)
