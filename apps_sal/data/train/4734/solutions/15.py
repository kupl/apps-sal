def bonus_time(salary, bonus):

    salary = int(salary)
    bonus = bool(bonus)

    if bonus is True:
        salary = salary * 10
    return "${}".format(salary)
