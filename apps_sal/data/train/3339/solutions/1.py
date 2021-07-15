def mystery(n):
    return [i for i in range(1, n + 1) if n%i == 0 and i%2]
