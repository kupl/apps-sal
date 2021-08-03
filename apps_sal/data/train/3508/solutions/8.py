def halving_sum(n):
    if n == 1:
        return 1
    else:
        return n + halving_sum(int(n / 2))
