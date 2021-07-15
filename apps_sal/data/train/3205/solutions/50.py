def is_divisible(n,x,y):
    flag = False
    if(not(n % x) and not(n % y)):
        flag = True
    return flag
