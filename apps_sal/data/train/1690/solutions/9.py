# cook your dish here
from collections import defaultdict
n, k = list(map(int, input().split()))
b = []
drel = defaultdict(list)
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    b.append(a[1:])
for i in range(n):
    for j in range(n):
        m = 0
        for l in b[j]:
            if l in b[i]:
                m += 1
            if m >= k:
                drel[i].append(j)
                break
visited = set()


def dfs(node):
    global ans
    visited.add(node)
    for i in drel[node]:
        if i not in visited:
            ans += 1
            dfs(i)


dfs(0)
print(ans + 1)
