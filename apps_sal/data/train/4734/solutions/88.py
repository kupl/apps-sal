def bonus_time(salary, bonus):
    if bonus == True:
        total = salary * 10
        return '$' + str(total)
    if bonus == False:
        return '$' + str(salary)
