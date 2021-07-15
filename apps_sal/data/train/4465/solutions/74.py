def super_size(n):
    s = sorted(list(str(n)))
    s.reverse()
    return int(''.join(s))
