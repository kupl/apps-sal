def is_divisible(n,x,y):
    a = n / x
    b = n / y
    return a.is_integer() and b.is_integer()
