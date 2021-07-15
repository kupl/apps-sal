def is_divisible(n,x,y):
    if x == 0 or y == 0: return False
    return n//x == n/x and n//y == n/y
