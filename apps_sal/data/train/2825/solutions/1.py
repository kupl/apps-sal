def even_magic(n):
    l = list(range(1, n * n + 1))
    for i in range(n * n // 2):
        (y, x) = (i // n % 4, i % n % 4)
        if y == x or x + y == 3:
            (l[i], l[n * n - 1 - i]) = (l[n * n - 1 - i], l[i])
    return [l[i * n:i * n + n] for i in range(n)]
