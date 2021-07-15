def bonus_time(salary, bonus):
    if bonus:
        payday = salary * 10
        return '$' + str(payday)
    else:
        return '$' + str(salary)
