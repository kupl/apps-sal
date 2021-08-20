from itertools import count


def count_squares(lines):

    def check(i, j, k):
        return lines[i + k][j] == lines[i][j + k] == lines[i + k][j + k] == '+' and all((lines[x][j] in '|+' for x in range(i + 1, i + k))) and all((lines[i][x] in '-+' for x in range(j + 1, j + k))) and all((lines[x][j + k] in '|+' for x in range(i + 1, i + k))) and all((lines[i + k][x] in '-+' for x in range(j + 1, j + k)))
    res = 0
    for (i, row) in enumerate(lines):
        for (j, c) in enumerate(row):
            if c == '+':
                for k in count(1):
                    try:
                        res += check(i, j, k)
                    except:
                        break
    return res
