def is_divisible(n,x,y):
    return all([n%m==0 for m in (x, y)])
