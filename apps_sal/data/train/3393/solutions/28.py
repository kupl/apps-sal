import math

def is_square(n):
    s = math.sqrt(n)
    return (s - math.floor(s)) == 0

def sds(n):
    s = 1 + (n**2 if n>1 else 0)
    l , r = 2, n//2
    while l < r:
        if (l*r) == n:
            s += l**2 + r**2
        l , r = l+1, n//(l+1)
    return s

def list_squared(m, n):  
    res = []
    for i in range(m,n):
        s_sum = sds(i)
        if is_square(s_sum):
            res.append([i, s_sum])
    return res
        

