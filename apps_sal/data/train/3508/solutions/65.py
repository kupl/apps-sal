def halving_sum(n): 
    r=n
    while(n>0):
        n//=2
        r+=n
    return r
