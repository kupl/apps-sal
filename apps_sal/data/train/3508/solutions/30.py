def halving_sum(n):
    return 1 if n // 1 == 1 else n // 1 + halving_sum((n // 1) / 2)
