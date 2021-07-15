def duty_free(price, discount, holiday_cost):
    return int(int(holiday_cost) / int(discount) / int(price) * 100)
