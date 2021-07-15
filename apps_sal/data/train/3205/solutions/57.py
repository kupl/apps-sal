def is_divisible(n,x,y):
    a = n % x
    b = n % y
    if (a or b) == 0:
        return True
    else:
        return False
