def halving_sum(n): 
    sm = 0
    i = 0
    while n // 2**i > 0:
        sm += n // 2**i
        i += 1
    return sm

