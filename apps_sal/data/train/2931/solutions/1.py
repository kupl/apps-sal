def count_cows(n):
    if isinstance(n, int):
        (a, b, c) = (1, 0, 0)
        for _ in range(n):
            (a, b, c) = (c, a, b + c)
        return a + b + c
