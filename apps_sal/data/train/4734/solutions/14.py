def bonus_time(salary, bonus):
    if bonus == True:
        return '$' + str(salary * 10)
    else:
        return '$' + str(salary)
