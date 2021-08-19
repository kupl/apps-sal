def bonus_time(salary, bonus):
    if bonus == True:
        k = str(salary * 10)
    else:
        k = str(salary)
    return '$' + k
