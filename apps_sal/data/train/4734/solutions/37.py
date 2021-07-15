def bonus_time(salary, bonus):
    s = salary*10
    if bonus is True:
        return "$"+str(s)
    if bonus is False:
        return "$"+str(salary)

