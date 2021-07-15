def is_divisible(n,x,y):
    if (x>n or y>n):
        return False
    else:
        if (n%x!=0 or n%y!=0):
            return False
        else:
            return True
