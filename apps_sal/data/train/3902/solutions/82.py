def duty_free(price, discount, holiday_cost):
    dsc_price = price * (1-discount)
    diff = price - dsc_price
    return int(holiday_cost / diff * 100)
