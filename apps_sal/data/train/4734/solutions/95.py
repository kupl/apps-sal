def bonus_time(salary, bonus):
    #your code here
    sum='$'
    if bonus==True: 
        salary=salary*10
        salary=str(salary)
        return sum+salary
    return sum+ str(salary)

