def halving_sum(n): 
    if n > 1 :
        n = n + halving_sum(n//2)
    return n
