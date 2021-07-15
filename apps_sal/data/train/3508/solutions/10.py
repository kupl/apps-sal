def halving_sum(n): 
    # your code here
    re = n
    while n > 1:
        n = n//2
        re += n
    return re
