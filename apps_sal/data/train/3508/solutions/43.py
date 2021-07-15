def halving_sum(n): 
    sum = n
    while n > 1:
        n //= 2 # n=n//2
        sum += n
    return sum
