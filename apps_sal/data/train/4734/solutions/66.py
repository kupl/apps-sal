def bonus_time(salary, bonus):
    # your code here
    if bonus == True:
        m = salary * 10
        return '$' + str(m)
    return '$' + str(salary)
