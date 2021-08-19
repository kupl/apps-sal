def pattern(n):
    return ''.join(((str((k + 1) % 10) * n).center(3 * n - 2) + '\n' for k in range(n - 1))) + (''.join((str((i + 1) % 10) for i in range(n - 1))) + n * str(n % 10) + ''.join((str(j % 10) for j in range(n - 1, 0, -1))) + '\n') * n + '\n'.join(((str(g % 10) * n).center(3 * n - 2) for g in range(n - 1, 0, -1)))
