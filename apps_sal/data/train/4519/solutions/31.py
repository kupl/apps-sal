def max_number(n):
    g = list(str(n))
    v = sorted (g, reverse = True)
    v = ''.join(v)
    return int(v)
