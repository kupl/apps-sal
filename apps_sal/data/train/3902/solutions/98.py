def duty_free(price, discount, holiday_cost):
    duty_free = price * (discount / 100)
    bottles = int(holiday_cost / duty_free)
    return bottles
