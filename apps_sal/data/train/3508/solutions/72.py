def halving_sum(n): 
    l=0
    while n!=1:
        l+=n
        n=n//2
    return l+1
