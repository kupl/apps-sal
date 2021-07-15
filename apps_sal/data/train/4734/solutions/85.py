def bonus_time(salary, bonus):
    result = str(salary*10) if bonus else str(salary)
    return "${}".format(result)
