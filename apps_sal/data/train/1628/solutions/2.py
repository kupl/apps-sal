def euler(n):
    res = 1.0*n
    p = 2
    while p*p <= n:
        if n%p == 0:
            while n%p == 0:
                n = n/p
            res *= (1.0 - (1.0/p) )
        p += 1
    
    if n > 1:
        res *= (1.0 - (1.0/n) )
    
    return int(res)

def proper_fractions(d):
    if d == 1:
        return 0
    return euler(d)
