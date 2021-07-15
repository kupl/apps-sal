def halving_sum(n): 
    # your code here
    total = n
    while n > 0:
        n = n//2
        total += n
    return total
    pass
