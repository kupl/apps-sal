def bonus_time(salary, bonus):
    if bonus:
        salary = salary * 10
    return str.format('${0}', salary)
