def halving_sum(n): 
    k = n
    t = n
    while k > 0:
        k = int(k /2)
        t+=k
    return t
