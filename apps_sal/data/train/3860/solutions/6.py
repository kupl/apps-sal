def how_many_apples(n):
    if n == 2:
        return 7
    if n == 3:
        return 25
    x = how_many_apples(n - 1) * (n - 1) + (n - 1) * (n - 3)
    for i in range(n):
        x = x * n // (n - 1) + 1
    return x
