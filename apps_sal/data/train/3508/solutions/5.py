def halving_sum(n):
    return n + halving_sum(n // 2) if n else 0
