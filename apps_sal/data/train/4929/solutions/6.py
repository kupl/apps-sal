def get_diagonale_code(grid: str) -> str:
    (i, j, res, move, M) = (0, 0, [], 1, [line.split() for line in grid.split('\n')])
    while i < len(M) and j < len(M[i]):
        res.append(M[i][j])
        move = 1 if i == 0 else -1 if i == len(M) - 1 else move
        (i, j) = (i + move, j + 1)
    return ''.join(res)
