def halving_sum(n): 
    if n<=1: return n
    return n + halving_sum(n//2)
