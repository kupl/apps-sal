def even_magic(n):
    return [[n * n - (y * n + x) if x % 4 == y % 4 or (x % 4 + y % 4) % 4 == 3 else y * n + x + 1 for x in range(n)] for y in range(n)]
