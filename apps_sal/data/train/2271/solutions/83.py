N, M = list(map(int, input().split()))
p_list = list(map(int, input().split()))
queries = [list(map(int, input().split())) for i in range(M)]
paths = [[] for i in range(N + 1)]
for a, b in queries:
    paths[a].append(b)
    paths[b].append(a)

groups = []
visited = [False] * (N + 1)
for start in range(N + 1):
    if visited[start] == True:
        continue
    queue = [start]
    t_group = set()
    t_group.add(start)
    visited[start] = True
    while queue:
        now = queue.pop()
        for next in paths[now]:
            if visited[next] == True:
                continue
            queue.append(next)
            t_group.add(next)
            visited[next] = True
    groups.append(t_group)

result = 0
for group in groups[1:]:
    result += sum(1 for m in group if p_list[m - 1] in group)

print(result)
