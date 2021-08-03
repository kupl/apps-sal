def max_number(n):
    r = sorted(list(str(n)))[::-1]
    k = ''.join(r)
    return int(k)
