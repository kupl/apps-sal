def bonus_time(salary, bonus):
    if(bonus == True):
        s = str(salary * 10)
        return "$" + s
    else:
        salary = str(salary)
        return "$" + salary
