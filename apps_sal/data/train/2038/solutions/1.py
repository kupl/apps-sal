import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = [''] * (n + 1)
g1 = [[] for _ in range(n + 1)]
g2 = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    g1[a].append(b)
    g2[b].append(a)
    deg[a] += 1
status = [0] * (n + 1)
q = collections.deque()
for i in range(1, n + 1):
    if deg[i] == 0:
        q.append(i)
while len(q) != 0:
    v = q.pop()
    status[v] = 1
    for u in g2[v]:
        deg[u] -= 1
        if deg[u] == 0:
            q.append(u)
if status.count(0) >= 2:
    print(-1)
else:
    status1 = [0] * (n + 1)
    status2 = [0] * (n + 1)
    for i in range(1, n + 1):
        if status1[i] == 0 and status2[i] == 0:
            ans[i] = 'A'
        else:
            ans[i] = 'E'
        if status1[i] == 0:
            q = collections.deque()
            q.append(i)
            while len(q) != 0:
                v = q.pop()
                status1[v] = 1
                for u in g1[v]:
                    if status1[u] == 0:
                        status1[u] = 1
                        q.append(u)
        if status2[i] == 0:
            q = collections.deque()
            q.append(i)
            while len(q) != 0:
                v = q.pop()
                status2[v] = 1
                for u in g2[v]:
                    if status2[u] == 0:
                        status2[u] = 1
                        q.append(u)
    print(ans.count('A'))
    print(''.join(map(str, ans[1:])))
