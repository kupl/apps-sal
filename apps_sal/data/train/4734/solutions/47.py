def bonus_time(salary, bonus):
    b = salary
    if bonus:
        b *= 10
    return '$' + str(b)
