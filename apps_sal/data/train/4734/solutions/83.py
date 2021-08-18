def bonus_time(salary, bonus):
    total = ''
    if bonus == True:
        return total + '$' + str(salary * 10)
    return total + '$' + str(salary)
