def count_pal(n):
    pal = lambda n: 9 * 10**((n-1)//2)
    return [pal(n), sum(pal(i) for i in range(1, n+1))]
