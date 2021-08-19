def bonus_time(salary, bonus):
    pay = salary * 10 if bonus else salary
    return f'${pay}'
