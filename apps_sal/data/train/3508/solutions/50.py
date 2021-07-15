def halving_sum(n): 
    sum = n
    while True:
        if n//2==0: break
        else      : n = n//2
        sum += n
    return sum
