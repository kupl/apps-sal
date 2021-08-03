def bonus_time(salary, bonus):
    b = salary * 10 if bonus else salary
    return "$" + str(b)
