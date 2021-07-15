def halving_sum(n): 
    return 1 if n<2 else n + halving_sum((int)(n/2))
    

