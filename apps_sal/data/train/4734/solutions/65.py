def bonus_time(salary, bonus):
    if bonus == True:
        new = salary * 10
        return str('$' + str(new))
    else:
        return str('$' + str(salary))
