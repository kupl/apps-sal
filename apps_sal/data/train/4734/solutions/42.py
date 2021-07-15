def bonus_time(salary, bonus):
    if bonus==True:
        return '$'+str(salary)+'0'
    elif bonus==False:
        return '$'+str(salary)
