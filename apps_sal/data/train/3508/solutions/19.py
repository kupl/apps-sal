def halving_sum(n): 
    result = 0

    while n:
        result += n
        n //= 2

    return result
