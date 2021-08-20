def pattern(n):
    return '\n'.join((''.join((str(n - j) for j in range(i + 1))) for i in range(n)))
