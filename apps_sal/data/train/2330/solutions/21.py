s = list(map(int, input()))
n = len(s)
if s[0]==0 or s[-1] == 1 or any(s[i]!=s[i] for i in range(n//2)):
    print((-1))
    return
G = [[] for i in range(n)]
cur = 0
for i in range(n-1):
    G[cur].append(i+1)
    G[i+1].append(cur)

    if s[i]:
        cur = i+1

root = n//2
from collections import deque
size = [1]*n
ans = [0]*n
edges = []
def bfs1(root):
    rev = [(root, -1)]
    for i in range(n):
        cur, par = rev[i]
        for to in G[cur]:
            if to != par:
                rev.append((to, cur))
    for i in reversed(list(range(1,n))):
        cur, par = rev[i]
        size[par] += size[cur]
        ans[size[cur]] = 1
        ans[n-size[cur]] = 1
        edges.append([cur+1, par+1])
bfs1(0)

if any(ans[i+1]!=s[i] for i in range(n-1)):
    print((-1))
    return

for i in edges:
    print((*i))

