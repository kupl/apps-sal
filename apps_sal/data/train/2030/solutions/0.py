from collections import defaultdict
from collections import deque
from functools import reduce
n, x, y = [int(x) for x in input().split()]
E = defaultdict(set)
for i in range(n-1):
    u, v = [int(x) for x in input().split()]
    E[u].add(v)
    E[v].add(u)

if x > y:
    for v in E:
        if len(E[v]) == n-1:
            print((n-2)*y + x)
            break
        elif len(E[v]) > 1:
            print((n-1)*y)
            break
else:
    visited = {v : False for v in E}
    stack = [1]
    topsorted = deque()
    while stack:
        v = stack.pop()
        if visited[v]: continue
        visited[v] = True
        topsorted.appendleft(v)
        stack.extend(E[v])
    chopped = set()
    ans = 0
    for v in topsorted:
        ans += max(0, len(E[v])-2)
        if len(E[v]) > 2:
            S = E[v].intersection(chopped)
            S1 = {S.pop(), S.pop()}
            for u in E[v]:
                if not u in S1:
                    E[u].remove(v)
            E[v].clear()
            E[v].update(S1)
        chopped.add(v)
    print(ans*y + (n-1-ans)*x)
        

