def pattern(n):
    return '\n'.join(['1'] + ['1' + '*' * (i - 1) + str(i) for i in range(2, n + 1)])
