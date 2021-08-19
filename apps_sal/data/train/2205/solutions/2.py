from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


(H, W, T) = list(map(int, input().split()))
Y = [[int(a) for a in input()] for _ in range(H)]
Q = deque([])
D = [-1] * (H * W)
for x in range(H * W):
    (i, j) = (x // W, x % W)
    y = Y[i][j]
    if i and Y[i - 1][j] == y or (i < H - 1 and Y[i + 1][j] == y) or (j and Y[i][j - 1] == y) or (j < W - 1 and Y[i][j + 1] == y):
        D[x] = 0
        Q.append(x)
while Q:
    x = Q.popleft()
    (i, j) = (x // W, x % W)
    for (di, dj) in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        (ni, nj) = (i + di, j + dj)
        if 0 <= ni < H and 0 <= nj < W:
            y = ni * W + nj
            if D[y] == -1:
                D[y] = D[x] + 1
                Q.append(y)
if D[0] < 0:
    D = [10 ** 18] * (H * W)
for _ in range(T):
    (i, j, p) = list(map(int, input().split()))
    (i, j) = (i - 1, j - 1)
    x = i * W + j
    print(Y[i][j] if max(p - D[x], 0) % 2 == 0 else Y[i][j] ^ 1)
