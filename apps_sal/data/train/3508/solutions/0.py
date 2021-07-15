def halving_sum(n): 
    s=0
    while n: 
        s+=n ; n>>=1
    return s
