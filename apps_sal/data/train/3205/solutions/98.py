def is_divisible(n,x,y):
    a = n%x
    b = n%y
    return False if bool(a+b) else True
