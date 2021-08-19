def pattern(n):
    return f'\n'.join([f'{str(i) * i}' for i in range(1, n + 1) if n >= 1])
