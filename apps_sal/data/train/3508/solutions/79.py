def halving_sum(n): 
    m = 0
    while n >= 1:
        m += n
        n //= 2
    return m
