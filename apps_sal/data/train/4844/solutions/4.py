(X, Y) = ({'l': -1, 'r': 1}, {'u': -1, 'd': 1})


def get_password(grid, directions):
    (result, (i, j)) = ([], next(((i, j) for (i, row) in enumerate(grid) for (j, c) in enumerate(row) if c == 'x')))
    for d in directions:
        (i, j) = (i + Y.get(d[0], 0), j + X.get(d[0], 0))
        if d[-1] == 'T':
            result.append(grid[i][j])
    return ''.join(result)
