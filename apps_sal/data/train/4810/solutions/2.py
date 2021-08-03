from operator import lt, gt


def mst(edges, inf, compare, min_max):
    Q = {v for vs, _ in edges for v in vs}
    C = dict.fromkeys(Q, inf)
    E = dict.fromkeys(Q)
    while Q:
        v = min_max(Q, key=C.get)
        Q.discard(v)
        candidates = ((edge, weight) for edge, weight in edges if v in edge)
        for edge, weight in candidates:
            v_, w = edge
            if w == v:
                w = v_
            if w in Q and compare(weight, C[w]):
                E[w], C[w] = edge, weight
        if E[v] is not None:
            yield E[v], C[v]


def make_spanning_tree(edges, t):
    return list(mst(
        edges,
        float('inf' if t == 'min' else '-inf'),
        lt if t == 'min' else gt,
        min if t == 'min' else max,
    ))
