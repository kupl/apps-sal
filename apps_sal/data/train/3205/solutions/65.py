def is_divisible(n,x,y):
    # We want to check if n is divisible by BOTH x AND Y
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False
