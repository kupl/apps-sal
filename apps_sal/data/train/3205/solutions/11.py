def is_divisible(n,x,y):
    return (False, True)[n%x==0 and n%y==0]
