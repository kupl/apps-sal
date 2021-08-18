import sys
t = int(sys.stdin.readline())


def identify(x, y):
    rows[x][y] = '2'

    r = 0
    if x == 0:
        r |= 1
    elif rows[x - 1][y] == '1':
        r |= identify(x - 1, y)
    if x == 7:
        r |= 4
    elif rows[x + 1][y] == '1':
        r |= identify(x + 1, y)
    if y == 0:
        r |= 2
    elif rows[x][y - 1] == '1':
        r |= identify(x, y - 1)
    if y == 7:
        r |= 8
    elif rows[x][y + 1] == '1':
        r |= identify(x, y + 1)
    return r


P = 21945

while t:
    t -= 1
    n = int(sys.stdin.readline()) - 3

    rows = [list(sys.stdin.readline().strip()) for i in range(8)]
    total = 0
    for i in range(8):
        for j in range(8):
            if rows[i][j] == '1':
                r = identify(i, j)
                if n == 0:
                    total += 1
                    continue
                if r == 0:
                    total += pow(2, 2 * n, P)
                elif r == 1 or r == 2 or r == 4 or r == 8:
                    total += pow(2, 2 * n - 1, P)
                    if r == 1 or r == 2:
                        total += pow(2, n, P)
                elif r == 5 or r == 10:
                    total += pow(2, n, P)
                elif r == 3 or r == 6 or r == 12 or r == 9:
                    total += pow(2, 2 * n - 2, P)
                    if r == 3:
                        total += 3 + 2 * pow(2, n - 1, P) - 2
                    elif r == 6 or r == 9:
                        total += pow(2, n - 1, P)
                elif r == 15:
                    total += 1
                else:
                    total += pow(2, n - 1, P)
                    if r == 11 or r == 7:
                        total += 1
    print(total % P)
