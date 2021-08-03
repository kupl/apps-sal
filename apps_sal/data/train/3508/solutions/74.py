def halving_sum(n):
    half = 0
    while n > 1:
        half += n
        n = n // 2
    return half + 1
