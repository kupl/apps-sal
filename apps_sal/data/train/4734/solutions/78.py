def bonus_time(salary, bonus):
    if bonus == True:
        salary *= 10
        a = "${}".format(salary)
        return a
    return "$" + str(salary)
