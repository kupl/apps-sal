from collections import defaultdict


def get_neighbors(edges):
    neighbors = defaultdict(set, {})
    for (v1, v2) in edges:
        neighbors[v1].add(v2)
        neighbors[v2].add(v1)
    return dict(neighbors)


def get_component(neighbors_map, root):
    if root not in neighbors_map:
        return {root}
    horizon = set(neighbors_map[root])
    component = {root}
    while horizon:
        new_node = horizon.pop()
        if new_node in component:
            continue
        component.add(new_node)
        new_neighbors = neighbors_map[new_node].difference(component)
        horizon |= new_neighbors
    return component


def fn(weights, edges, root):
    neihgbors_map = get_neighbors(edges)
    if root not in neihgbors_map:
        return weights[root]
    first_component = get_component(neihgbors_map, root)
    neihgbors_map = {k: v for (k, v) in list(neihgbors_map.items()) if k in first_component}
    degrees = {}
    leaves = []
    for (n, neigh) in list(neihgbors_map.items()):
        degrees[n] = len(neigh)
        if len(neigh) == 1 and n != root:
            leaves.append(n)
    extra_values = defaultdict(int, {})
    max_extra = 0
    removed_set = set()
    while leaves:
        leaf = leaves.pop()
        value = weights[leaf] + extra_values[leaf]
        parent = neihgbors_map.pop(leaf).pop()
        neihgbors_map[parent].remove(leaf)
        degrees[parent] -= 1
        if degrees[parent] == 1 and parent != root:
            leaves.append(parent)
        mm = max(extra_values[parent], value)
        extra_values[parent] = mm
        max_extra = max(mm, max_extra)
        removed_set.add(leaf)
    return sum((weights[n] for n in neihgbors_map)) + max_extra


def print_answer(source):
    (n, m) = list(map(int, source().split()))
    weights = list(map(int, source().split()))
    edges = [[int(k) - 1 for k in source().split()] for _ in range(m)]
    root = int(source()) - 1
    print(fn(weights, edges, root))


print_answer(input)
if False:
    from string_source import string_source
    print_answer(string_source('3 2\n1 1335 2\n2 1\n3 2\n2'))
    from string_source import string_source
    print_answer(string_source('1 0\n1000000000\n1'))
    print_answer(string_source('10 12\n    1 7 1 9 3 3 6 30 1 10\n    1 2\n    1 3\n    3 5\n    5 7\n    2 3\n    5 4\n    6 9\n    4 6\n    3 7\n    6 8\n    9 4\n    9 10\n    6'))
    print_answer(string_source('5 7\n    2 2 8 6 9\n    1 2\n    1 3\n    2 4\n    3 2\n    4 5\n    2 5\n    1 5\n    2'))
    source = string_source('3 2\n1 1335 2\n2 1\n3 2\n2')
    (n, m) = list(map(int, source().split()))
    weights = list(map(int, source().split()))
    edges = [[int(k) - 1 for k in source().split()] for _ in range(m)]
    root = int(source())
    fn(weights, edges, root)
    from graphviz import Graph
    dot = Graph(format='png', name='xx', filename=f'_files/temp/graph.png')
    for (idx, w) in enumerate(weights):
        dot.node(str(idx), label=f'{idx} - {w}')
    for (s, e) in edges:
        dot.edge(str(s), str(e))
    dot.view(cleanup=True)
    sum(weights)
