def thirt(n):
    p = [1, 10, 9, 12, 3, 4]
    ns = sum((int(c) * p[i % len(p)] for (i, c) in enumerate(str(n)[::-1])))
    return ns if ns == n else thirt(ns)
