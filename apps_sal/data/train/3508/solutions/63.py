def halving_sum(n): 
    result = 0
    while n > 0:
        result += n
        n = int(n / 2)
    return result
