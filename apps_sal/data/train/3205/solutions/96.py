def is_divisible(n,x,y):
    if n > 0 and x > 0 and y > 0:
        if n % x == 0 and n % y == 0:
            return True
        elif n == 0 :
            return True
        else:
            return False
    else:
        return 0
