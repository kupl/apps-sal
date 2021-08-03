from collections import *
n = int(input())
fa = [0, 0] + [int(i) for i in input().split()]
s = [0] + [int(i) for i in input().split()]
g = [[] for i in range(n + 1)]
for x in range(2, len(fa)):
    g[fa[x]].append(x)

sub = [0] * (n + 1)
q = deque([1])
rcr = []
while(q):
    x = q.popleft()
    rcr.append(x)
    for y in g[x]:
        q.append(y)
rcr.reverse()

inf = int(1e10)
s1 = [inf if i == -1 else i for i in s]
for x in rcr:
    sub[x] = s1[x]
    if g[x]:
        sub[x] = min(sub[x], min([sub[y] for y in g[x]]))

dp = [0] * (n + 1)
a = [0] * (n + 1)
q = deque(g[1])
a[1] = s[1] if s[1] != -1 else 0
dp[1] = a[1]
ans = a[1]
ok = 1
while(q):
    x = q.popleft()
    if sub[x] == inf:
        a[x] = 0
    else:
        if s[x] == -1:
            a[x] = sub[x] - dp[fa[x]]
        else:
            a[x] = s[x] - dp[fa[x]]
    if a[x] < 0:
        ok = 0
        break
    dp[x] = dp[fa[x]] + a[x]
    ans += a[x]
    for y in g[x]:
        q.append(y)

print(ans) if ok else print(-1)
