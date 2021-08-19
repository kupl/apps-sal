def max_number(n):
    n = ''.join(sorted(str(n), reverse=True))
    return int(n)
