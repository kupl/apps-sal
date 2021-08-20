from math import ceil, sqrt, factorial, gcd
from sys import stdin


def input():
    return stdin.readline().strip()


(n, m) = map(int, input().split())
ans = [0 for i in range(n)]
nextl = [i + 1 for i in range(n + 2)]
for j in range(m):
    (l, r, x) = map(int, input().split())
    i = l
    while i <= r:
        if ans[i - 1] == 0 and i != x:
            ans[i - 1] = x
        a = nextl[i]
        if i < x:
            nextl[i] = x
        else:
            nextl[i] = r + 1
        i = a
print(*ans)
