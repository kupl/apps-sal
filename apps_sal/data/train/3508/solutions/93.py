def halving_sum(n): 
    a = 0
    while n >= 1:
        a += n
        n *= 1/2
        n  = int(n)
    return a
