from collections import deque
import sys


for _ in range(int(sys.stdin.readline())):
    n, m = list(map(int, sys.stdin.readline().split()))
    g = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = list(map(int, sys.stdin.readline().split()))
        g[a].append(b)
        g[b].append(a)
        
    k = [[], [1]]
    color = [-1] * (n + 1)
    m = deque([1])
    color[1] = 1
    while m:
        u = m.popleft()
        for v in g[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                k[color[v]].append(v)
                m.append(v) 
                
    if len(k[0]) <= n // 2:
        print(len(k[0]))
        print(*k[0])
        
    else:
        print(len(k[1]))
        print(*k[1])

