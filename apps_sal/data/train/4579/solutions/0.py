def pattern(n):
    return '\n'.join((''.join((str((n - min(j, i)) % 10) for j in range(n))) for i in range(max(n, 0))))
