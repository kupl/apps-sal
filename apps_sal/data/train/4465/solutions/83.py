def super_size(n):
    w = list(str(n))
    w.sort(reverse=True)
    return int(''.join(w))
