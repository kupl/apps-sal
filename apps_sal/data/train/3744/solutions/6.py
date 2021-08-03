def oddest(a):
    def f(x): return 1e6 if x == -1 else x % 2 and 1 + f(x // 2) or 0
    a = [(x, f(x)) for x in a]
    n = max((y for x, y in a), default=-1)
    a = [x for x, y in a if y == n]
    if len(a) == 1:
        return a[0]
