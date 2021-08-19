def bonus_time(salary, bonus):
    return '${}'.format(str(salary * 10)) if bonus == True else '${}'.format(salary)
