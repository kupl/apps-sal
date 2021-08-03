def pattern(n):
    return '\n'.join(f'{str (i) * i}' for i in range(1, n + 1) if n >= 1)
