from collections import defaultdict


def processes(start, end, processes):
    d = defaultdict(list)
    for (process, x, y) in processes:
        d[x].append((y, process))
    (visited, nodes) = (set(), [(start, [])])
    while nodes:
        next = []
        for (node, path) in nodes:
            if node in visited:
                continue
            if node == end:
                return path
            visited.add(node)
            for (y, process) in d[node]:
                next.append((y, path + [process]))
        nodes = next
    return []
