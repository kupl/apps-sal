def halving_sum(n): 
    return n and n + halving_sum(n>>1)
