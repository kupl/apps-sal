def duty_free(price, discount, holiday_cost):
    result = holiday_cost//(price*discount*0.01)
    return(round(result))

