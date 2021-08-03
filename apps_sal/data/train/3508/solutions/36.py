def halving_sum(n):
    return n if n <= 1 else halving_sum(n // 2) + n
