def bonus_time(salary, bonus):
    #your code here
    x=lambda salary,bonus: str('$'+str(salary*10)) if(bonus==True) else str('$'+str(salary))
    return x(salary,bonus)
