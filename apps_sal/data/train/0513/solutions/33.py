import bisect
import sys
sys.setrecursionlimit(10**7)

n = int(input())
a = [0] + list(map(int, input().split()))
t = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    t[u].append(v)
    t[v].append(u)

m = 10**18
dp = [m] * (n + 1)
ans = [1] * (n + 1)
checked = [False] * (n + 1)
checked[1] = True
changes = []


def search(x):
    ind = bisect.bisect_left(dp, a[x])
    changes.append((ind, dp[ind]))
    dp[ind] = a[x]
    ans[x] = bisect.bisect_left(dp, m)

    for i in t[x]:
        if not checked[i]:
            checked[i] = True
            search(i)

    b, c = changes.pop()
    dp[b] = c


search(1)
for i in ans[1:]:
    print(i)
