def pattern(n):
    pattern = ''
    if n < 1:
        return pattern
    for i in range(1, n):
        pattern = pattern + str(i) * i + '\n'
    pattern = pattern + str(n) * n
    return pattern
