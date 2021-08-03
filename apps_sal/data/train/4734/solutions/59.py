def bonus_time(salary, bonus):
    if bonus == True:
        s = salary * 10
        s = str(s)
        return '$' + s
    else:
        s = str(salary)
        return '$' + s
