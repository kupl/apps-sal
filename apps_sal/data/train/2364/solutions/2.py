from collections import deque
from itertools import accumulate
import sys
input = sys.stdin.readline


def bfs(x):
    DIS = [-1] * (n + 1)
    Q = deque([x])
    DIS[x] = 0
    while Q:
        x = Q.pop()
        for to in E[x]:
            if DIS[to] == -1:
                DIS[to] = DIS[x] + 1
                Q.appendleft(to)
    return DIS


t = int(input())
for tests in range(t):
    (n, m, a, b, c) = list(map(int, input().split()))
    P = sorted(map(int, input().split()))
    S = [0] + list(accumulate(P))
    E = [[] for i in range(n + 1)]
    for i in range(m):
        (x, y) = list(map(int, input().split()))
        E[x].append(y)
        E[y].append(x)
    DIS_A = bfs(a)
    DIS_B = bfs(b)
    DIS_C = bfs(c)
    ANS = 1 << 63
    if DIS_A[b] + DIS_B[c] <= m and ANS > S[DIS_A[b] + DIS_B[c]]:
        ANS = S[DIS_A[b] + DIS_B[c]]
    for i in range(1, n + 1):
        d2 = DIS_B[i]
        d1 = DIS_A[i] + DIS_C[i]
        if d1 + d2 > m:
            continue
        if ANS > S[d2] * 2 + S[d1 + d2] - S[d2]:
            ANS = S[d2] * 2 + S[d1 + d2] - S[d2]
    print(ANS)
