from collections import defaultdict
from itertools import product


def solve(mouse, n, m):

    shadow = [[0 for i in range(m)]for j in range(n)]
    for i, j in product(list(range(n)), list(range(m))):
        if mouse[i][j] == 1:
            if i > 0:
                shadow[i - 1][j] += 1
            if j > 0:
                shadow[i][j - 1] += 1
            if i < n - 1:
                shadow[i + 1][j] += 1
            if j < m - 1:
                shadow[i][j + 1] += 1

    dp = defaultdict(int)

    dp[(0, 0, 0)] = dp[(0, 0, 1)] = shadow[0][0] - mouse[0][0]

    for i in range(1, m):
        dp[(0, i, 0)] = dp[(0, i, 1)] = shadow[0][i] - mouse[0][i] + dp[(0, i - 1, 0)]

    for i in range(1, n):
        dp[(i, 0, 0)] = dp[(i, 0, 1)] = shadow[i][0] - mouse[i][0] + dp[(i - 1, 0, 1)]

    for i, j in product(list(range(1, n)), list(range(1, m))):
        a = shadow[i][j] - mouse[i][j]
        b = a
        a += min(dp[(i, j - 1, 0)], dp[(i, j - 1, 1)] - mouse[i - 1][j])
        b += min(dp[(i - 1, j, 1)], dp[(i - 1, j, 0)] - mouse[i][j - 1])
        dp[(i, j, 0)] = a
        dp[(i, j, 1)] = b

    return min(dp[(n - 1, m - 1, 0)], dp[(n - 1, m - 1, 1)]) + mouse[0][0] + mouse[n - 1][m - 1]


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    mouse = []
    for i in range(n):
        x = input()
        mouse.append(list(map(int, x)))
    print(solve(mouse, n, m))
