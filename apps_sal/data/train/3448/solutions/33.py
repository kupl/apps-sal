def f(n):
    return None if type(n) in [str, float] or n < 1 else sum([i for i in range(0, n + 1)])
