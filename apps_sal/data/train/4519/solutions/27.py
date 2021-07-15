def max_number(n):
    return int(''.join([i for i in sorted(list(str(n)))[::-1]]))
