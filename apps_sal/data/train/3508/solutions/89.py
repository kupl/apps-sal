def halving_sum(n): 
    delit = 2
    sum = n
    while n > 0:
        n = n//delit
        delit*2
        sum+=n
    return sum
