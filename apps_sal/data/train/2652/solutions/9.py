def count_squares(lines):
    def is_topleft(i, j):
        b = lines[i][j] == '+'
        b = b and i + 1 < len(lines) and j < len(lines[i + 1]) and lines[i + 1][j] in '|+'
        b = b and j + 1 < len(lines[i]) and lines[i][j + 1] in '-+'
        return b

    def is_square(i, j, k):
        b = i + k < len(lines) and all(j + k < len(lines[r]) for r in range(i, i + k + 1))
        b = b and lines[i][j] == lines[i][j + k] == lines[i + k][j] == lines[i + k][j + k] == '+'
        if k > 1:
            b = b and all(lines[r][j] in '+|' and lines[r][j + k] in '+|' for r in range(i, i + k + 1))
            b = b and all(lines[i][c] in '+-' and lines[i + k][c] in '+-'for c in range(j, j + k + 1))
        return b
    cnt = 0
    for i in range(len(lines) - 1):
        for j in range(len(lines[i]) - 1):
            if is_topleft(i, j):
                for k in range(1, len(lines[i]) - j):
                    if is_square(i, j, k):
                        cnt += 1
    return cnt
