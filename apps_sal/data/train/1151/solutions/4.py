from collections import deque, defaultdict


def addEdge(graph, u, v):

    graph[u].append(v)


def bfs(graph, start):
    explored = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


def delete(graph, n):
    try:
        del graph[n]
    except KeyError:
        pass
    for i in graph:
        try:
            graph[i].remove(n)
        except ValueError:
            continue


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(m):
        u, v = list(map(str, input().split()))
        addEdge(graph, u, v)
        addEdge(graph, v, u)
    cnt = 0

    dele = []
    for i in range(n):
        if str(i) in dele:

            continue
        else:
            path = bfs(graph, str(i))
            for j in path:
                delete(graph, j)
                dele.append(j)

        cnt += 1

    print(cnt)
