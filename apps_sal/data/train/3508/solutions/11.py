def halving_sum(n):
    return n + halving_sum(n >> 1) if n > 1 else n
