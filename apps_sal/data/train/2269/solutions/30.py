import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n,m = map(int, input().split())
G = [[1]*n for i in range(n)]
for i in range(n):
    G[i][i] = 0
for i in range(m):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    G[a][b] = 0
    G[b][a] = 0

from collections import deque

used = [0]*n
tmp = []

def bfs(start):
    if used[start]:
        return True
    d = {-1:0, 1:0}
    que = deque()
    que.append((start, 1))
    while que:
        cur, flag = que.popleft()
        if used[cur] == flag:
            continue
        elif used[cur]:
            return False
        used[cur] = flag
        d[flag] += 1
        for to in range(n):
            if G[cur][to] and used[to] == 0:
                que.append((to, -flag))
    tmp.append(list(d.values()))
    return True

if not all(bfs(i) for i in range(n)):
    print(-1)
else:
    s = set([0])
    target = (n+1)//2
    for l in tmp:
        t = set()
        for a in l:
            for b in s:
                if a+b <= target:
                    t.add(a+b)
        s = t
    k = max(s)
    l = n-k
    ans = k*(k-1)//2 + l*(l-1)//2
    print(ans)
