def duty_free(price, discount, holiday_cost):
    a = price*(discount/100)
    b = holiday_cost//a
    b = int(b)
    return b
print(duty_free(12, 50, 1000))
