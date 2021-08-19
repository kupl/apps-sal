def max_number(n):
    n = list(map(int, str(n)))
    n = sorted(n, reverse=True)
    new_n = int(''.join(map(str, n)))
    return new_n
