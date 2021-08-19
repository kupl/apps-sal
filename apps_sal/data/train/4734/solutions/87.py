def bonus_time(salary, bonus):
    new_salary = salary * 10
    if bonus == True:
        return '$' + str(new_salary)
    return '$' + str(salary)
