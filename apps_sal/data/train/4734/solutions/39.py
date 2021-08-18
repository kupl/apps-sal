def bonus_time(salary, bonus):
    if bonus == True:
        result = "$" + str(salary * 10)
    elif bonus == False:
        result = "$" + str(salary)
    return result
