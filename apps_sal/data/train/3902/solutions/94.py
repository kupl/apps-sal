def duty_free(price, discount, holiday_cost):
    x=discount/100
    y=price*x
    z=holiday_cost//y
    return int(z)
