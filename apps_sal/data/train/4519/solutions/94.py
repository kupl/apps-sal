def max_number(n):
    n = ''.join(sorted(list(str(n)))[::-1])
    return int(n)
