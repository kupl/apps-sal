def even_magic(n):
    n2_1 = n ** 2 + 1
    return [
        [n2_1 - (i * n + j + 1) if i % 4 == j % 4 or (i + j) % 4 == 3 else i * n + j + 1 for j in range(n)]
        for i in range(n)
    ]
