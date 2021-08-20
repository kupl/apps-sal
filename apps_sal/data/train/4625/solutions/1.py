from collections import deque


def processes(start, end, graph):
    Q = deque([[i, []] for i in graph if i[1] == start])
    visited = set()
    while Q:
        ((p, s, e), path) = Q.popleft()
        path.append(p)
        visited.add((s, e))
        if e == end:
            return path
        for k in graph:
            if k[1] == e and tuple(k[1:]) not in visited:
                Q.append([k, path[:]])
    return []
