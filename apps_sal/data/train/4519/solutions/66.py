def max_number(n):
    x = list(str(n))
    x.sort(reverse=True)
    return int(''.join((y for y in x)))
