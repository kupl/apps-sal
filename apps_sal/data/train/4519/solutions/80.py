def max_number(n):
    d = str(n)
    q = sorted(d, reverse=True)
    w = ''.join(q)
    return int(w)
