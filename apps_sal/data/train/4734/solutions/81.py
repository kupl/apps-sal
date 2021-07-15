def bonus_time(salary, bonus):
    x = salary;
    y = 10 * salary
    if bonus:
        return '$'+ str(y)
    else:
        return '$'+ str(x)
