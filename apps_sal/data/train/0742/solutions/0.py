import random


def sign(i):
    if i > 0:
        return 1
    elif i <= 0:
        return 0


bleh = []
for _ in range(int(input())):
    p = list(map(int, input().rstrip().split()))
    max_rows = len(p)
    if all([x == 0 for x in p]):
        print(1)
        continue
    if max_rows <= 1:
        bleh.append(max_rows)
        continue
    max_pow = max_rows - 1
    if len(p) % 2 != 0 and len(p) > 0:
        p.append(0)
    max_col = len(p) // 2

    rows = [[0 for _ in range(max_col)] for _ in range(max_rows)]
    rows[0] = p[::2]
    rows[1] = p[1::2]
    if sign(rows[0][0]) != sign(rows[1][0]):
        print(0)
        continue

    for r in range(2, max_rows):
        for n in range(max_col - 1):
            rows[r][n] = rows[r - 1][0] * rows[r - 2][n + 1] - rows[r - 2][0] * rows[r - 1][n + 1]

    last = sign(rows[0][0])
    flag = 1
    for i in range(1, len(rows)):
        curr = sign(rows[i][0])
        if rows[r] == [0 for _ in range(max_col)]:
            for n in range(max_col):
                rows[r][n] = rows[r - 1][n] * (max_pow + 4 - (r + 1) - 2 * (n + 1))

        elif rows[i][0] == 0:
            if any([x != 0 for x in rows[i]]):
                flag = 0
                break
            else:
                curr = last
        if curr != last:
            flag = 0
            break
        last = curr
    print(flag)
