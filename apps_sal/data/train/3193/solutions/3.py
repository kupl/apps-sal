def stairs(n):
    return '\n'.join(' '.join([str(j % 10) for j in range(1, i + 1)] + [str(j % 10) for j in range(i, 0, -1)]).rjust(4 * n - 1) for i in range(1, n + 1))
