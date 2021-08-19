def bonus_time(salary, bonus):
    # your code here
    new_salary = salary * 10
    if bonus == True:
        return "$" + str(new_salary)
    return "$" + str(salary)
