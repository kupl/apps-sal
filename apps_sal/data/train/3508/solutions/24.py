def halving_sum(n): 
    return n if n == 1 else n + halving_sum(n // 2)
