def bonus_time(salary, bonus):
    if bonus == True:
        salary = salary * 10
    amt = str(salary)
    return '${}'.format(amt)
