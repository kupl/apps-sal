def checkchoose(m, n):
    from math import factorial as f
    a = 0
    while a <= n // 2:
        if m == f(n) / (f(a) * f(n - a)):
            return(a)
        else:
            a += 1
    return(-1)
