def halving_sum(n):
    result = n
    denom = 2
    while n // denom > 0:
        result += n // denom
        denom *= 2
    return result
