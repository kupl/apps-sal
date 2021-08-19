def pattern(n):
    return '\n'.join([(n - 1 - i) * ' ' + ''.join((str(j % 10) for j in range(1, n + 1))) + i * ' ' for i in range(n)])
