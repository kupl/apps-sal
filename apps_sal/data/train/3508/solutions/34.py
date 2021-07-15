def halving_sum(n): 
    if n//2 < 1:
        return n
    if n//2 == 1:
        return n + 1
    return n + halving_sum(n//2)
