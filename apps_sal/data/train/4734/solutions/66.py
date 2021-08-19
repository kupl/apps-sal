def bonus_time(salary, bonus):
    if bonus == True:
        m = salary * 10
        return '$' + str(m)
    return '$' + str(salary)
