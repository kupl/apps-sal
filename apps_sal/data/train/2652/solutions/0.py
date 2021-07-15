def count_squares(lines):
    def s(i, j, z):
        try:
            return (
                '+' == lines[i+z][j] == lines[i][j+z] == lines[i+z][j+z]
                and all(lines[i][c]   in '-+' for c in range(j+1, j+z))
                and all(lines[i+z][c] in '-+' for c in range(j+1, j+z))
                and all(lines[r][j]   in '|+' for r in range(i+1, i+z))
                and all(lines[r][j+z] in '|+' for r in range(i+1, i+z))
            )
        except IndexError:
            return 0
    return sum(
        x == '+' and sum(s(i, j, z) for z in range(1, min(len(lines)-i, len(row)-j)))
        for i, row in enumerate(lines[:-1])
        for j, x in enumerate(row[:-1])
    )

