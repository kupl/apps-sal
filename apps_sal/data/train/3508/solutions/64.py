def halving_sum(n):  
    if n > 1:
        n += halving_sum(n//2)
    return n

