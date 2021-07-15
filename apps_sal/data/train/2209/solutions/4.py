import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for i in range(n - 1)]

tree = [[] for i in range(n)]
for a, b in info:
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)
    
max_ = n - 1
for v in range(n):
    cnt = 0
    for nxt_v in tree[v]:
        if len(tree[nxt_v]) == 1:
            cnt += 1
    max_ -= max(cnt - 1, 0)
    
    
visited = [-1] * n
q = deque([0])
visited[0] = 0
while q:
    v = q.popleft()
    for nxt_v in tree[v]:
        if visited[nxt_v] != -1:
            continue
        visited[nxt_v] = visited[v] + 1
        q.append(nxt_v)


min_ = 3
for i in range(n):
    if len(tree[i]) == 1:
        if visited[i] % 2 == 0:
            break
else:
    min_ = 1

for i in range(n):
    if len(tree[i]) == 1:
        if (visited[i] + 1) % 2 == 0:
            break
else:
    min_ = 1
print(min_, max_)
