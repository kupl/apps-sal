def halving_sum(n):
    total = 0
    
    while True:
        if n == 0:
            break
        else:
            total += (n)
            n = n // 2
    
    return total
