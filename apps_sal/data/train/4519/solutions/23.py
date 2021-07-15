def max_number(n):
    s = sorted(str(n))
    st = ''.join(s)[::-1]
    return int(st)
