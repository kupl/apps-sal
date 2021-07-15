def points(n):
    return 1 + 4 * sum(map(lambda x: int((n * n - x * x)**0.5),range(0,n+1)))
