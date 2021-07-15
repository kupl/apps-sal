def super_size(n):
    l = list(str(n))
    l = sorted(l, reverse = True)
    return int(''.join(l))
