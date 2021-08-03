def bonus_time(salary, bonus):
    dollar = "$"
    if bonus == True:
        result = str(salary * 10)
        return dollar + result
    elif bonus == False:
        return "$" + str(salary)
