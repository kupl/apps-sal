def pattern(n):
    return '\n'.join(''.join(str((n - min(i, j))%10) for j in range(n)) for i in range(n))
