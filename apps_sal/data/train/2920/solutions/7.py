def pattern(n):
    return '\n'.join(''.join(str(j) for j in range(n, i, -1)) for i in range(n - 1, -1, -1))
