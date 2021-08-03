def bonus_time(salary, bonus):
    if bonus == True:
        amount = salary * 10
        return "$" + str(amount)
    elif bonus == False:
        return "$" + str(salary)
