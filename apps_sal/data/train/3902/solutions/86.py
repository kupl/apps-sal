def duty_free(price, discount, holiday_cost):
    discount = discount / 100
    save = (price * discount)
    price = holiday_cost / save
    return int(price)
