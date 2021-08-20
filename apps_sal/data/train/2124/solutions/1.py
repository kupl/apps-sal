from collections import defaultdict, deque
adj = defaultdict(lambda: defaultdict(lambda: 0))


def bfs(graph, inicio, destino, parent):
    parent.clear()
    queue = deque()
    queue.append([inicio, float('Inf')])
    parent[inicio] = -2
    while len(queue):
        (current, flow) = queue.popleft()
        for i in adj[current]:
            if parent[i] == -1 and graph[current][i] > 0:
                parent[i] = current
                flow = min(flow, graph[current][i])
                if i == destino:
                    return flow
                queue.append((i, flow))
    return 0


def maxflow(graph, inicio, destino):
    flow = 0
    parent = defaultdict(lambda: -1)
    while True:
        t = bfs(graph, inicio, destino, parent)
        if t:
            flow += t
            current = destino
            while current != inicio:
                prev = parent[current]
                graph[prev][current] -= t
                graph[current][prev] += t
                current = prev
        else:
            break
    return flow


(n, m, x) = [int(i) for i in input().split()]
for _ in range(m):
    t = [int(i) for i in input().split()]
    adj[t[0]][t[1]] = t[2]


def check(k):
    meh = defaultdict(lambda: defaultdict(lambda: 0))
    for i in adj:
        for j in adj[i]:
            ww = adj[i][j] // k
            meh[i][j] = ww
    flow = maxflow(meh, 1, n)
    return flow


lo = 1 / x
hi = check(1)
for _ in range(70):
    mid = (hi + lo) / 2
    if check(mid) >= x:
        lo = mid
    else:
        hi = mid
print(format(lo * x, '.9f'))
