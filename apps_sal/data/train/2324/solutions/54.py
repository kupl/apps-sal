ai = lambda: list(map(int,input().split()))
ai_ = lambda: [int(x)-1 for x in input().split()]

n = int(input())

path = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = ai_()
    path[a].append(b)
    path[b].append(a)

from collections import deque
q = deque()
q.append(0)

d1 = [float('inf') for _ in range(n)]
d1[0] = 0
w = set()
while q:
    v = q.popleft()
    w.add(v)
    for vv in path[v]:
        if vv not in w:
            d1[vv] = d1[v] + 1
            q.append(vv)


q = deque()
q.append(n-1)

dn = [float('inf') for _ in range(n)]
dn[n-1] = 0
w = set()
while q:
    v = q.popleft()
    w.add(v)
    for vv in path[v]:
        if vv not in w:
            dn[vv] = dn[v] + 1
            q.append(vv)


d = [1 if d1[v] <= dn[v] else -1 for v in range(n)]

if sum(d) > 0:
    print('Fennec')
else:
    print('Snuke')

