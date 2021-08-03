def find_bee_heads(hive):
    for i, row in enumerate(hive):
        for j, x in enumerate(row):
            if x == 'b':
                yield i, j


def count_ee(hive, r, c, i, j):
    return sum(
        0 <= i + di * 2 < r and 0 <= j + dj * 2 < c and hive[i + di][j + dj] == hive[i + di * 2][j + dj * 2] == 'e'
        for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    )


def how_many_bees(hive):
    hive = hive or []
    r = len(hive)
    c = r and len(hive[0])
    return sum(count_ee(hive, r, c, i, j) for i, j in find_bee_heads(hive))
