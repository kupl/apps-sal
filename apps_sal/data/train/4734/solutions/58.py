def bonus_time(salary, bonus):

    def x(salary, bonus):
        return str('$' + str(salary * 10)) if bonus == True else str('$' + str(salary))
    return x(salary, bonus)
