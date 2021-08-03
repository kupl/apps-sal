def halving_sum(n):
    return 1 if n <= 1 else n + halving_sum(n // 2)
