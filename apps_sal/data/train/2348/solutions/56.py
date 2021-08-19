from bisect import bisect
import sys
input = sys.stdin.readline
n = int(input())
x = list(map(int, input().split()))
l = int(input())
m = 20
par = [[-1] * n for i in range(m)]
for i in range(n):
    j = bisect(x, x[i] + l) - 1
    par[0][i] = j
for i in range(m - 1):
    for j in range(n):
        par[i + 1][j] = par[i][par[i][j]]


def hoge(x, y):
    k = 0
    for i in range(m)[::-1]:
        if par[i][x] < y:
            k += 1 << i
            x = par[i][x]
    return k + 1


q = int(input())
ans = []
for i in range(q):
    (a, b) = map(int, input().split())
    (a, b) = (a - 1, b - 1)
    if a > b:
        (a, b) = (b, a)
    print(hoge(a, b))
