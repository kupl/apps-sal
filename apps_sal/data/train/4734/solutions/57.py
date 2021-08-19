def bonus_time(salary, bonus):
    return f"{'$' + str(salary * 10)}" if bonus else f"{'$' + str(salary)}"
