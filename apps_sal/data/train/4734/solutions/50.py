def bonus_time(salary, bonus):
    if bonus:
        return F"${((salary * 10))}"
    return F"${salary}"
