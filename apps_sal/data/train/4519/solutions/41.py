def max_number(n):
    res = int(''.join(sorted(str(n), reverse=True)))
    return res
