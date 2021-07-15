def bonus_time(salary, bonus):
    total = salary
    if bonus:
        salary *= 10
    return '$%d' % (salary)
