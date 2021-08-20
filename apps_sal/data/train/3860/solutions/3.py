def how_many_apples(n):
    if n == 2:
        return 7
    return n ** (n - 1) * n - n + 1
