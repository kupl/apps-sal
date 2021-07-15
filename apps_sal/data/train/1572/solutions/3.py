# cook your dish here
from collections import defaultdict
from collections import deque
a = list(map(int,input().split()))
n = a[0]
v = a[1:n+1]
p = a[n+1:]
ans = -1000000000
boss = 1
graph = defaultdict(set)
for i in range(n):
    if p[i] == -1:
        boss = i+1
        continue
    else:
        graph[p[i]].add(i+1)
        
def bfs(boss, graph, n):
    nonlocal ans
    que = deque([])
    que.append(boss)
    while que:
        key = que.popleft()
        for item in graph[key]:
            que.append(item)
            z = v[key-1] - v[item-1]
            if(ans<z):
                ans = z 
            if v[key-1] > v[item-1]:
                v[item-1] = v[key-1]
bfs(boss, graph, n)
print(ans)

        
    

