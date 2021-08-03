n = int(input())
ab = [list(map(int, input().split())) for i in range(n - 1)]
graph = [[] for i in range(n + 1)]
visited = [0 for i in range(n + 1)]
root = 1
stack = [root]
for a, b in ab:
    graph[a].append(b)
    graph[b].append(a)
visited[0] = -1
visited[root] = 1
while stack:
    x = stack.pop()
    if x == n:
        break
    for y in graph[x]:
        if visited[y] == 0:
            stack.append(y)
            visited[y] = visited[x] + 1
dist = visited[n] - 1
way = n
while True:
    if visited[way] == dist // 2 + 2:
        border = way
        break
    for y in graph[way]:
        if visited[y] == visited[way] - 1:
            way = y
stack = [1]
visited = [0 for i in range(n + 1)]
visited[border] = 1
fen = 0
while stack:
    x = stack.pop()
    fen += 1
    visited[x] = 1
    for y in graph[x]:
        if visited[y] == 0:
            stack.append(y)
snk = n - fen
if fen > snk:
    print("Fennec")
else:
    print("Snuke")
