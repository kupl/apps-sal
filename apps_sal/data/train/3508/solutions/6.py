def halving_sum(n): 
    L=[n]
    for i in range(1,n+1):
        a = n//(2**i)
        if a not in L:
            L.append(a)
    return sum(L)
