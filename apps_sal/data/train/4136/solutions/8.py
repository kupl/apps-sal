def cake_slice(n):
    if n == 0:
        return 1
    else:
        return 2 + sum(iter(range(2,n+1)))
