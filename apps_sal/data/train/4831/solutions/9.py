def solved(string):
    n = len(string)
    return ''.join(sorted(string[:n // 2] + string[n // 2 + n % 2:]))
