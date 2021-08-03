def bonus_time(salary, bonus):
    if bonus == True:
        result = salary * 10
    else:
        result = salary

    return f"${result}"
