n, edges_num = list(map(int, input().split()))
edges = set(tuple(map(int, input().split())) for _ in range(edges_num))
nodes = set(range(1, n + 1))
comps = 0
comp_q = []
while nodes:
    if comp_q:
        u = comp_q.pop()
    else:
        u = nodes.pop()
        comps += 1
    zero_set = {v for v in nodes if (u, v) not in edges and (v, u) not in edges}
    nodes -= zero_set
    comp_q += zero_set
print(comps - 1)
