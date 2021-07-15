def halving_sum(n):
    return 1 if n == 1 else sum([n//(2**i) for i in range(0, n//2) if n//(2**i) >=1])
