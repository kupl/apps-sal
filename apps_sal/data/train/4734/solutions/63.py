def bonus_time(salary, bonus):
    return "$%d" % (salary * 10 if bonus == True else salary)
