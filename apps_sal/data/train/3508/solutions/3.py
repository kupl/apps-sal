def halving_sum(n):
    result = n

    while n >= 1:
        n //= 2
        result += n

    return result
