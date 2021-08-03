def make_triangle(m, n):
    size = ((8 * (n - m + 1) + 1)**.5 - 1) / 2
    if size % 1:
        return ''

    grid = [[' ' for _ in range(int(size) * 2 - 1)] for _ in range(int(size))]
    i, j = 0, int(size - 1)
    grid[i][j] = str(m % 10)

    while m < n:
        for inc, dec in [(1, 1), (0, -2), (-1, 1)]:
            while 0 <= i + inc < size and 0 <= j + dec < size * 2 - 1 and grid[i + inc][j + dec].isspace():
                i, j, m = i + inc, j + dec, m + 1
                grid[i][j] = str(m % 10)

    return '\n'.join([''.join(i).rstrip() for i in grid])
