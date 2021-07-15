def duty_free(price, discount, holiday_cost):
    sale_price = price * discount / 100
    return int(holiday_cost / sale_price)
