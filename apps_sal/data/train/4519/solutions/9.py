def max_number(n):
    s = list(str(n))
    s.sort()
    res = s[::-1]
    return int(''.join(res))
