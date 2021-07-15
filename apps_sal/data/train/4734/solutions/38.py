def bonus_time(salary, bonus):
    i = 0
    if bonus is True:
        i = salary*10
    if bonus is False:
        i = salary
    return '$'+ str(i)

