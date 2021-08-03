def halving_sum(n):
    return sum(n >> i for i in range(15))
