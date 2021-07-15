def max_number(n):
    tmp = list(str(n))
    return int(''.join(sorted(tmp, reverse=True)))
