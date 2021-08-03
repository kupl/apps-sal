def max_number(n):
    p = [str(i) for i in str(n)]
    p = sorted(p, reverse=True)
    p = ''.join(p)
    p = int(p)
    return p
