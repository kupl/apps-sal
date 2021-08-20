def connect_the_dots(paper: str) -> str:
    res = list(map(list, paper.splitlines()))
    d = [v for (_, v) in sorted({c: (i, j) for (i, row) in enumerate(res) for (j, c) in enumerate(row) if c != ' '}.items())]
    for ((prev_i, prev_j), (i, j)) in zip(d, d[1:]):
        if prev_i == i:
            for x in range(min(j, prev_j), max(j, prev_j) + 1):
                res[i][x] = '*'
        elif prev_j == j:
            for x in range(min(i, prev_i), max(i, prev_i) + 1):
                res[x][j] = '*'
        else:
            (di, dj) = ([1, -1][prev_i > i], [1, -1][prev_j > j])
            for x in range(abs(prev_j - j) + 1):
                res[prev_i + x * di][prev_j + x * dj] = '*'
    return '\n'.join(map(''.join, res)) + '\n'
