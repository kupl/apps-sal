def processes(start, end, processes):
    '''Dijkstra's shortest path algorithm'''
    q = [(start, [])]
    visited = set()

    while q:
        s, path = q.pop(0)
        if s == end:
            return path
        visited.add(s)
        for p in [x for x in processes if x[1] == s]:
            if not p[2] in visited:
                q.append((p[2], path + [p[0]]))
    return []
