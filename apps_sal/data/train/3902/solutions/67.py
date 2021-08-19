def duty_free(price, discount, holiday_cost):
    price2 = price * (discount / 100)
    cost = holiday_cost / price2
    return int(cost)
