def bonus_time(salary, bonus):
    x = str(int(salary) * 10)
    y = str(int(salary))
    if bonus == True:
        return str('$')+ x
    else:
        return str('$')+ y
