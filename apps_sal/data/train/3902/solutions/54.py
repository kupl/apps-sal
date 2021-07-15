def duty_free(price, discount, holiday_cost):
    savings = price * discount/100
    sol = holiday_cost/savings
    return int(sol)
