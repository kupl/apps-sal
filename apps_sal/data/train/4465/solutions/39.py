def super_size(n):
    p = list(str(n))
    p.sort()
    return int(''.join(reversed(p)))
