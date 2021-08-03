def bonus_time(salary, bonus):
    if bonus == True:
        s = salary * 10
    else:
        s = salary
    return str('$' + str(s))
