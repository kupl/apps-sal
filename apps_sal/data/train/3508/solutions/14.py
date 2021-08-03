def halving_sum(n):
    if n < 1:
        return 0
    else:
        return n + halving_sum(n // 2)
