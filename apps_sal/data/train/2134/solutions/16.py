import collections
from collections import defaultdict
n = int(input())
par = [int(i) for i in input().split() if i != '\n']
suma = [int(i) for i in input().split() if i != '\n']
graph = defaultdict(list)
for i in range(n - 1):
    graph[i + 2].append(par[i])
    graph[par[i]].append(i + 2)
weight = [0] * (n + 1)
weight[1] = suma[0]
queue = collections.deque([1])
visited = set()
visited.add(1)
ok = True
while queue:
    vertex = queue.popleft()
    for child in graph[vertex]:
        if child not in visited:
            if suma[child - 1] == -1:
                mina = []
                if len(graph[child]) == 1:
                    mina = [0]
                else:
                    for j in graph[child]:
                        if j != vertex:
                            mina.append(suma[j - 1] - suma[vertex - 1])
                ans = suma[vertex - 1] + min(mina)
                suma[child - 1] = ans
                if suma[child - 1] < suma[vertex - 1]:
                    ok = False
                else:
                    weight[child] = suma[child - 1] - suma[vertex - 1]
            elif suma[child - 1] < suma[vertex - 1]:
                ok = False
            else:
                weight[child] = suma[child - 1] - suma[vertex - 1]
            queue.append(child)
            visited.add(child)
if ok == True:
    print(sum(weight))
else:
    print(-1)
