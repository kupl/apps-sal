from sys import stdin
import numpy as np


def sin():
    return stdin.readline()


for _ in range(int(sin())):
    n, m, k = list(map(int, sin().split()))
    grid = np.zeros([n, m])
    ans = 4 * k
    for i in range(k):
        r, c = list(map(int, sin().split()))
        r -= 1
        c -= 1
        if r > 0 and grid[r - 1][c] == 1:
            ans -= 2
        if c > 0 and grid[r][c - 1] == 1:
            ans -= 2
        if c < m - 1 and grid[r][c + 1] == 1:
            ans -= 2
        if r < n - 1 and grid[r + 1][c] == 1:
            ans -= 2
        grid[r][c] = 1
    print(ans)
