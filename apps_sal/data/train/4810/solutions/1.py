def make_spanning_tree(edges, t):
    edges = sorted(edges, key=lambda x: x[1], reverse=t == 'max')
    span, vert = [], {}

    for edge in edges:
        ((a, b), _), (subA, subB) = edge, map(vert.get, edge[0])

        if a == b or subA is not None and subA is subB:
            continue

        if subA and subB:
            subA |= subB
            for v in subB:
                vert[v] = subA
        else:
            subSpan = subA or subB or set()
            for v in (a, b):
                subSpan.add(v)
                vert[v] = subSpan
        span.append(edge)

    return span
