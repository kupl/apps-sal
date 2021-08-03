def bonus_time(salary, bonus):
    return "$" + str(salary) if bonus is False else "$" + str(salary * 10)
