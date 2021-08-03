def bonus_time(salary, bonus):
    i = salary * 10
    k = salary
    if bonus == True:
        return "$" + str(i)
    else:
        return "$" + str(k)
