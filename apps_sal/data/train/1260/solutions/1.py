from collections import defaultdict
t = int(input())
for _ in range(t):
    (n, m, k) = map(int, input().split())
    graph = defaultdict(lambda: [])
    for _ in range(m):
        (u, v) = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    museums = list(map(int, input().split()))
    visited = [0] * n
    lista = []
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            stack = [i]
            counter = museums[i]
            while len(stack) > 0:
                u = stack.pop()
                for v in graph[u]:
                    if visited[v] == 0:
                        counter += museums[v]
                        stack.append(v)
                        visited[v] = 1
            lista.append(counter)
    if len(lista) < k:
        print(-1)
    else:
        lista.sort()
        counter = 0
        id0 = 0
        id1 = len(lista) - 1
        for i in range(k):
            if i % 2 == 0:
                counter += lista[id1]
                id1 -= 1
            else:
                counter += lista[id0]
                id0 += 1
        print(counter)
