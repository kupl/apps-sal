def bonus_time(salary, bonus):
    pay = str(salary * 10) if bonus else str(salary)
    return '${}'.format(pay)
