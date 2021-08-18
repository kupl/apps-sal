import sys


def toposort(graph):
    res = []
    found = [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(~node)
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack += graph[node]

    for node in res:
        if any(found[nei] for nei in graph[node]):
            return None
        found[node] = 0

    return res[::-1]


inp = [int(x) for x in sys.stdin.read().split()]
ii = 0
t = inp[0]
ii += 1
for _ in range(t):
    n, m = inp[ii:ii + 2]
    ii += 2
    graph = [[] for _ in range(n + 1)]
    undir = []
    for i in range(m):
        type, u, v = inp[ii:ii + 3]
        ii += 3
        if type == 0:
            undir.append([u, v])
        else:
            graph[u].append(v)
    order = toposort(graph)
    if not order:
        print("NO")
        continue
    print("YES")
    index = [0] * (n + 1)
    for i in range(n + 1):
        index[order[i]] = i
    for i in range(n + 1):
        for u in graph[i]:
            print(i, u)
    for u, v in undir:
        if index[u] < index[v]:
            print(u, v)
        else:
            print(v, u)
