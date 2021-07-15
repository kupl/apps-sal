def max_number(n):
    b = list(str(n))
    c = sorted(b)
    d = c[::-1]
    x = ''.join(e for e in d)
    return int(x)
