def pattern(n):
    if n % 2 != 0:
        n = n - 1
    return '' if n <= 1 else '\n'.join([str(i) * i for i in range(1, n + 1) if i % 2 == 0])
