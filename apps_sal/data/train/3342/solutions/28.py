def pattern(n):
    return ''.join(['{}{}'.format(str(i) * int(i), '\n') for i in range(1, n + 1)])[:-1]
