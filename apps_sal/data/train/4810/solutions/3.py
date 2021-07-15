def make_spanning_tree(edges, t):
    id = {}
    edges.sort(key=lambda x: x[1], reverse=t == 'max')
    spanning_tree = []
    for (u, v), cost in edges:
        if u not in id: id[u] = u
        if v not in id: id[v] = v
        if id[u] != id[v]:
            id = {x: y if y != id[v] else id[u] for x, y in id.items()}
            spanning_tree.append((u + v, cost))
    return spanning_tree
