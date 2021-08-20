def duty_free(price, discount, holiday_cost):
    savings = price * (discount / 100)
    numberNeeded = holiday_cost / savings
    return int(numberNeeded)
