def halving_sum(n): 
    div = 2
    total = n
    while n//div:
        total += n//div
        div *= 2
    return total
