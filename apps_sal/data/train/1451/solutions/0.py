# cook your dish here
for _ in range(int(input())):
    N, M = [int(x) for x in input().split()]
    edges = [0] * M
    dir = {}
    nodes = [[] for j in range(N + 1)]
    ind = [0] * (N + 1)
    graph = {}
    final_edges = []
    for i in range(M):
        u, v = [int(x) for x in input().split()]
        nodes[u].append(v)
        nodes[v].append(u)
        dir[(u, v)] = 1
        dir[(v, u)] = 0
        ind[v] += 1
        graph[(u, v)] = graph[(v, u)] = i
        final_edges.append([u, v])
    if M % 2 != 0:
        print(-1)
        continue
    for i in range(M):
        u, v = final_edges[i]
        if ind[u] % 2 != 0 and ind[v] % 2 != 0:
            d = dir[(u, v)]
            if d:
                ind[u] += 1
                ind[v] -= 1
                dir[(u, v)] = 0
                dir[(v, u)] = 1
                edges[i] = abs(edges[i] - 1)
            else:
                ind[u] -= 1
                ind[v] += 1
                dir[(u, v)] = 1
                dir[(v, u)] = 0
                edges[i] = abs(edges[i] - 1)
    s = []
    for i in range(1, N + 1):
        if ind[i] % 2:
            s.append(i)
    while s:
        set1 = set()
        for u in s:
            if ind[u] % 2:
                v = nodes[u][0]
                d = dir[(u, v)]
                index = graph[(u, v)]
                set1.add(v)
                if d:
                    ind[u] += 1
                    ind[v] -= 1
                    dir[(u, v)] = 1
                    dir[(v, u)] = 1
                    edges[index] = abs(edges[index] - 1)
                else:
                    ind[u] -= 1
                    ind[v] += 1
                    dir[(u, v)] = 1
                    dir[(v, u)] = 0
                    edges[index] = abs(edges[index] - 1)

        s = set1
    print(*edges)
