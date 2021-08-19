def detect_triangle(adj):
    for x in range(len(adj)):
        for y in adj[x]:
            if not set(adj[x]).isdisjoint(adj[y]):
                return True


for _ in range(int(input())):
    (n, m) = map(int, input().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        (u, v) = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    h = []
    for i in range(len(graph)):
        h.append(len(graph[i]))
    h1 = max(h)
    if h1 >= 3:
        print(h1)
        continue
    if detect_triangle(graph):
        print(3)
        continue
    print(h1)
