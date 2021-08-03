def even_magic(n):
    numbers, p = iter(list(range(1, n * n + 1))), 0
    main_grid = [[next(numbers) for _ in range(n)] for _ in range(n)]
    def A(s, se, see, e, ee, eee): return list(zip(range(s, se, see), range(e, ee, eee)))
    for i in range(n // 4):
        o = 0
        for j in range(n // 4):
            for k, l in A(p, p + 4, 1, o, o + 4, 1) + A(p, p + 4, 1, o + 3, o - 1, -1):
                main_grid[k][l] = ((n ** 2) + 1) - main_grid[k][l]
            o += 4
        p += 4
    return main_grid
