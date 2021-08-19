def even_magic(n):
    return [[y % 4 in (x % 4, 3 - x % 4) and n * n - n * y - x or n * y + x + 1 for x in range(n)] for y in range(n)]
