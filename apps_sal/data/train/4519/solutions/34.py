def max_number(n):
    arr = list(str(n))
    s = sorted(arr)[::-1]
    return int(''.join(s))
