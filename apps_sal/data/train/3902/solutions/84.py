def duty_free(price, discount, holiday_cost):
    save = price * (discount / 100)
    bottles = holiday_cost / save
    return int(bottles)
