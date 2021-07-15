def bonus_time(salary, bonus):
    x = salary * 10
    
    if bonus == True:
        return f'${x}'
    elif bonus == False:
        return f'${salary}'
