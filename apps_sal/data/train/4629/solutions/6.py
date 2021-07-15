def penalty(p):
    n = len(max(p, key=int))
    return ''.join(sorted(p, key=lambda x: (x.ljust(n, x[-1]), -len(x))))
