from bisect import bisect_right
import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())


sys.setrecursionlimit(10**9)

N = int(input())
Xs = list(mapint())
L = int(input())

nex = [[0] * N for _ in range(32)]
for i in range(N):
    now = Xs[i]
    idx = bisect_right(Xs, now + L) - 1
    nex[0][i] = idx

for i in range(1, 32):
    for j in range(N):
        nex[i][j] = nex[i - 1][nex[i - 1][j]]

Q = int(input())
for _ in range(Q):
    a, b = mapint()
    if a > b:
        a, b = b, a
    a, b = a - 1, b - 1
    cnt = 0
    for i in range(31, -1, -1):
        if nex[i][a] < b:
            cnt += 2**i
            a = nex[i][a]
    if a != b:
        cnt += 1
    print(cnt)
