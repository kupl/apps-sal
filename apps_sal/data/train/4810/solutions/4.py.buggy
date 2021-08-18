def make_spanning_tree(edges, t):
    edges.sort(reverse=True)
    last_node = ord(edges[0][0][0]) - 65
    edges.sort()
    edges.sort(key=lambda edges: edges[1])

    if(t == 'max'):
        edges.reverse()

    nonlocal parent
    parent = [int(x) for x in range(last_node + 10000)]
    result = []

    for edge in edges:
        startNode = ord(edge[0][0]) - 65
        endnode = ord(edge[0][1]) - 65

        if(Find(startNode) != Find(endnode)):
            Union(startNode, endnode)
            result.append(edge)

    return result


def Find(x):
    if(x == parent[x]):
        return x
    else:
        p = Find(parent[x])
        parent[x] = p
        return p


def Union(x, y):
    x = Find(x)
    y = Find(y)

    if(x != y):
        parent[y] = x
