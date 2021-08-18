from bisect import bisect_left
import sys
n = int(input())
A = list(map(int, input().split()))
g = [[]for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

sys.setrecursionlimit(10**6)

lastdp = [10**9 + 1] * n
recode = [[10**9 + 1]for i in range(n)]
ans = [0] * n


def rec(me, parent):
    nonlocal lastdp
    a = A[me]
    point = bisect_left(lastdp, a)
    recode[point].append(a)
    lastdp[point] = a
    tmpans = bisect_left(lastdp, 10**9 + 1)
    ans[me] = tmpans

    for child in g[me]:
        if child != parent:
            rec(child, me)

    recode[point].pop()
    lastdp[point] = recode[point][-1]
    return


rec(0, -1)
print(*ans, sep='\n')
