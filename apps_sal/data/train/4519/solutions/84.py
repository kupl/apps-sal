def max_number(n):
    l = list(str(n))
    k = sorted(l)
    return int(''.join((i for i in k[::-1])))
