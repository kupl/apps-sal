def duty_free(price, discount, holiday_cost):
    save = price * discount / 100.0
    return int(holiday_cost / save)
# hard, should in the 1kyu
